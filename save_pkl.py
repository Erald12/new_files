import requests
import base64

# Replace these with your actual GitHub details
GITHUB_TOKEN = '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'
REPO_OWNER = 'Erald12'
REPO_NAME = 'Neat-model-for-trading-8'
FILE_PATH = 'best_genome2.pkl'
GITHUB_FILE_PATH = 'best_genome2.pkl'
COMMIT_MESSAGE = 'Add best_genome2.pkl'

# Read the file content
with open(FILE_PATH, 'rb') as file:
    content = base64.b64encode(file.read()).decode('utf-8')

# Define the API URL for the file path
url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{GITHUB_FILE_PATH}'

# Set up the headers with the token
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Prepare the payload
data = {
    'message': COMMIT_MESSAGE,
    'content': content
}

# Check if the file already exists
response = requests.get(url, headers=headers)
if response.status_code == 200:
    # If the file exists, add SHA to the payload to update it
    data['sha'] = response.json()['sha']

# Upload the file
response = requests.put(url, headers=headers, json=data)

if response.status_code in [200, 201]:
    print(f"File uploaded successfully: {response.json()['content']['html_url']}")
else:
    print(f"Failed to upload file: {response.status_code}, {response.json()}")
