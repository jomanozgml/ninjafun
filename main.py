import json
from google.cloud import firestore
from page_parser import *
client = firestore.Client()

# Gets webpage OG and saves to the document


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

    affected_doc.set({
        u'positionDesc': text,
        u'positionTitle': get_og_title(soup),
        u'snippet': get_og_description(soup)
    })


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

# [START functions_firebase_firestore]


def hello_firestore(data, context):
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
# [END functions_firebase_firestore]


# [START functions_firebase_auth]
def hello_auth(data, context):
    """ Triggered by creation or deletion of a Firebase Auth user object.
     Args:
            data (dict): The event payload.
            context (google.cloud.functions.Context): Metadata for the event.
    """
    print('Function triggered by creation/deletion of user: %s' % data["uid"])
    print('Created at: %s' % data["metadata"]["createdAt"])

    if 'email' in data:
        print('Email: %s' % data["email"])
# [END functions_firebase_auth]


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
