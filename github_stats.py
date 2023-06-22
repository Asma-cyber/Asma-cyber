import requests

# Set up the API requests
base_url = 'https://api.github.com/'
username = 'Asma-cyber'

# Set your Personal Access Token
token = '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'

# Set the headers with the PAT
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Make API requests for different stats
endpoints = [
    f'users/{username}/stats/contributors',
    f'users/{username}/stats/commit_activity',
    f'users/{username}/stats/code_frequency',
    # Add more endpoints as needed
]

for endpoint in endpoints:
    url = base_url + endpoint
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract and process the stats
        stats = response.json()
        # Display or process the stats as desired
        print(stats)
    else:
        # Handle the case where the request was not successful
        print(f"Error: {response.status_code} - {response.json()['message']}")
