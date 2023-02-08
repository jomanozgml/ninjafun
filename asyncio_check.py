# Checks asyncio operation with simple function
# Simple function that checks the operation of asyncio function on google cloud deployment.
# Gets the asyncio>'original' string from firebase and converts to uppercase
# Asyncio operation is the asyncio.sleep(15); 15 seconds delay
import asyncio
from google.cloud import firestore
client = firestore.Client()

async def test_asyncio():
    await asyncio.sleep(15)
        
def asyncio_check(data, context):
    path_parts = context.resource.split('/documents/')[1].split('/')
    collection_path = path_parts[0]
    document_path = '/'.join(path_parts[1:])

    affected_doc = client.collection(collection_path).document(document_path)

    cur_value = data["value"]["fields"]["original"]["stringValue"]
    new_value = cur_value.upper()
    asyncio.run(test_asyncio())

    if cur_value != new_value:
        print(f'Replacing value: {cur_value} --> {new_value}')
        affected_doc.set({
            u'original': new_value
        })
    else:
        print('Value is already upper-case.')