# [START functions_firebase_firestore]


# def hello_firestore(data, context):
#     """ Triggered by a change to a Firestore document.
#     Args:
#         data (dict): The event payload.
#         context (google.cloud.functions.Context): Metadata for the event.
#     """
#     trigger_resource = context.resource

#     print('Function triggered by change to: %s' % trigger_resource)

#     print('\nOld value:')
#     print(json.dumps(data["oldValue"]))

#     print('\nNew value:')
#     print(json.dumps(data["value"]))
# # [END functions_firebase_firestore]


# # [START functions_firebase_auth]
# def hello_auth(data, context):
#     """ Triggered by creation or deletion of a Firebase Auth user object.
#      Args:
#             data (dict): The event payload.
#             context (google.cloud.functions.Context): Metadata for the event.
#     """
#     print('Function triggered by creation/deletion of user: %s' % data["uid"])
#     print('Created at: %s' % data["metadata"]["createdAt"])

#     if 'email' in data:
#         print('Email: %s' % data["email"])
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
