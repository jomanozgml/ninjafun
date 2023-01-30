import json
from google.cloud import firestore
from page_parser import *
import asyncio
from indeed_fetch import *
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

    if 'indeed' in vacancy_url:
        async def fetch_vacancy_details():
            page = await get_page_indeed(vacancy_url)
            return await get_title(page), await get_description(page)
            
        title, text = asyncio.get_event_loop().run_until_complete(fetch_vacancy_details())
    
    else:
        soup = get_page(vacancy_url)
        title = get_og_title(soup)
        desc = get_og_description(soup)
        tags = soup.select("p, h2, h3, h4, h5, h6, ul")
        # print(tags)
        # [type(item) for item in list(soup.children)]
        text = [item.text+'\n' for item in list(tags)]
    
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

