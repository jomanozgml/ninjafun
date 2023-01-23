import json
from google.cloud import firestore
from page_parser import *
client = firestore.Client()

def fetch_vacancy(data, context):
    """ Triggered by a change to a Firestore document.
    Args:
        data (dict): The event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """
    trigger_resource = context.resource

    print('Function triggered by change to: %s' % trigger_resource)

    print('\nOld value:')
    print(json.dumps(data["oldValue"]))

    print('\nNew value:')
    print(json.dumps(data["value"]))
    # path_parts = context.resource.split('/documents/')[1].split('/')
    # collection_path = path_parts[0]
    # document_path = '/'.join(path_parts[1:])

    # affected_doc = client.collection(collection_path).document(document_path)

    vacancy_url = data["value"]["fields"]["url"]["stringValue"]

    print(f'fetch url: {vacancy_url}')

    soup = get_page(vacancy_url)

    print(f'title: {get_og_title(soup)}')
    print(f'desc: {get_og_description(soup)}')

    tags = soup.select("p, h1, h2, h3, h4, h5, h6, strong, ul")

    print(tags)

    # [type(item) for item in list(soup.children)]
    text = [item.text+'\n' for item in list(tags)]

    print(text)

    path_parts = context.resource.split('/documents/')[1].split('/')
    collection_path = path_parts[0]
    document_path = '/'.join(path_parts[1:])

    affected_doc = client.collection(collection_path).document(document_path)

    affected_doc.update({
        u'positionDesc': text,
        u'positionTitle': get_og_title(soup),
        u'snippet': get_og_description(soup)
    })

