import json

import requests
import time
#Please enter your username and a unique folder name to upload your docs.
API_TOKEN = 'ADD-YOUR-API-TOKEN-HERE'
API_BASE_URL = 'https://aihub.instabase.com/api'
API_HEADERS = {
'Authorization': f'Bearer q6pmoNqVzvdZ2q0mi8X3E5sg7xIsmj'
}
APP_NAME = 'EXAMPLE-APP-NAME' #Please enter your app name
# Step 1: Run App
run_app_payload = json.dumps({
"input_dir": "input_file_dir",
"name": APP_NAME
# optional: "owner": "<owner-name", if not specified, assumes it is your
username
})
url = f'{API_BASE_URL}/v2/zero-shot-idp/projects/app/run'
run_app_resp = requests.post(url, headers=API_HEADERS, data=run_app_payload)
job_id = run_app_resp.json().get('job_id')
print(f'App Running: {job_id}')
return job_id
