import requests

# Replace with your information
organization_url = "https://dev.azure.com/<your_organization>"
access_token = "<your_personal_access_token>"
project_name = "<your_project_name>"
pipeline_id = "<your_pipeline_id>"

# Construct API endpoint URL
api_url = f"{organization_url}/_apis/pipelines/{project_name}/pipelines/{pipeline_id}/runs?api-version=6.0-preview.1"

# Set headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# Optional: Specify parameters for the pipeline run (e.g., variables)
# data = {
#     "variables": {
#         "var1": "value1",
#         "var2": "value2"
#     }
# }

# Send POST request
response = requests.post(api_url, headers=headers)

# Check for successful response
if response.status_code == 201:
    print("Pipeline triggered successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
