
Database Structure
==================

* **admin**

* **user**/{uid}/
  User private data. No one else has access to here accept for the user.

* **user**/{uid}/**vacancy**/{vacancyId}/
  * _attributes_:
    * url - url of the vacancy
  Actual vacancy fetch using Python. When the document is created the function
  will trigger. It will read the 'url' property and try to fetch the vacancy from
  that url. If successful, it will try to parse it and save the parsed text into
  this same document.


**Deploying functions**


gcloud functions deploy make_upper_case \
  --entry-point make_upper_case \
  --runtime python37 \
  --trigger-event "providers/cloud.firestore/eventTypes/document.write" \
  --trigger-resource "projects/jsninja-4f26c/databases/(default)/documents/messages/{pushId}"

Deploy fetch_vacancy function:

gcloud functions deploy fetch_vacancy \
  --entry-point fetch_vacancy \
  --runtime python37 \
  --trigger-event "providers/cloud.firestore/eventTypes/document.create" \
  --trigger-resource "projects/jsninja-4f26c/databases/(default)/documents/user/{userId}/vacancy/{vacId}"

