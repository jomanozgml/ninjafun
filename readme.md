
Deploy test function:

gcloud functions deploy make_upper_case \
  --entry-point make_upper_case \
  --runtime python37 \
  --trigger-event "providers/cloud.firestore/eventTypes/document.write" \
  --trigger-resource "projects/jsninja-4f26c/databases/(default)/documents/messages/{pushId}"

Deploy fetch_vacancy function:

gcloud functions deploy fetch_vacancy \
  --entry-point fetch_vacancy \
  --runtime python37 \
  --trigger-event "providers/cloud.firestore/eventTypes/document.write" \
  --trigger-resource "projects/jsninja-4f26c/databases/(default)/documents/vacancy/{vacId}"

