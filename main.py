from google.cloud import firestore
from page_parser import *
client = firestore.Client()

# Gets webpage OG and saves to the document
def fetch_vacancy(data, context):
    path_parts = context.resource.split('/documents/')[1].split('/')
    collection_path = path_parts[0]
    document_path = '/'.join(path_parts[1:])

    affected_doc = client.collection(collection_path).document(document_path)

    cur_value = data["value"]["fields"]["url"]["stringValue"]

    print(f'fetch url: {cur_value}')

    soup = get_page(cur_value)

    print(f'title: {get_og_title(soup)}')
    print(f'desc: {get_og_description(soup)}')

    tags = soup.select("p, ul")

    print(tags)

    # [type(item) for item in list(soup.children)]
    text = [item.text+'\n' for item in list(tags)]

    print(text)

    


# Converts strings added to /messages/{pushId}/original to uppercase
def make_upper_case(data, context):
    path_parts = context.resource.split('/documents/')[1].split('/')
    collection_path = path_parts[0]
    document_path = '/'.join(path_parts[1:])

    affected_doc = client.collection(collection_path).document(document_path)

    cur_value = data["value"]["fields"]["original"]["stringValue"]
    new_value = cur_value.upper()

    if cur_value != new_value:
        print(f'Replacing value: {cur_value} --> {new_value}')
        affected_doc.set({
            u'original': new_value
        })
    else:
        # Value is already upper-case
        # Don't perform a second write (which can trigger an infinite loop)
        print('Value is already upper-case.')

# from flask import jsonify
# import firebase_admin
# from firebase_admin import auth

# Initialize the app without credentials, as the function gets it from context
# firebase_admin.initialize_app()


# def verifyRequest(request):
#     authorization = request.headers.get('Authorization')
#     token = authorization.split('Bearer ')[1]
#     try:
#         # This will fail in every situation BUT successful authentication
#         decode_token = auth.verify_id_token(id_token=token)
#     except Exception as e:
#         print('Authorization failed')
#         print(e)
#         return jsonify({
#         'data': {
#             'status': 'Authorization failed'
#         }})

#     print('Authorization suceeded')
#     return jsonify({
#         'data': {
#             'status': 'Authorization succeeded'
#         }})

