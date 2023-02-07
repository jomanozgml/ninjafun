import json
from google.cloud import firestore
from page_parser import *
from indeed_fetch2 import *
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

    vacancy_url = data["value"]["fields"]["url"]["stringValue"]

    print(f'fetch url: {vacancy_url}')

    # Condition to check if the url is from indeed [or dynamic webpage]
    if 'indeed' in vacancy_url:
        # title, text = asyncio.run(get_details_indeed(vacancy_url))
        title, text = get_details_indeed(vacancy_url)
    # For static webpage
    else:
        title, text = get_page(vacancy_url)
    
    print(f'Title: {title}')
    print(text)

    path_parts = context.resource.split('/documents/')[1].split('/')
    collection_path = path_parts[0]
    document_path = '/'.join(path_parts[1:])

    affected_doc = client.collection(collection_path).document(document_path)

    affected_doc.update({
        u'positionDesc': text,
        u'positionTitle': title
    })