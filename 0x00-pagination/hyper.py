#!/usr/bin/python3
import requests
from os import getenv
# Replace 'YOUR_TOKEN' with your GitHub personal access token
TOKEN = getenv('token')

# Initial API endpoint for listing repositories
url = 'https://api.github.com/user/repos'
params = {'per_page': 10, 'page': 1}

# Initialize a list to store all repositories
all_repositories = []

while True:
    # Make a request to the GitHub API with your access token
    response = requests.get(url, params=params, headers={'Authorization': f'token {TOKEN}'})
    
    # Check if the response is successful
    if response.status_code == 200:
        # Parse the JSON response
        repositories = response.json()
        
        # Add the repositories from this page to the list
        all_repositories.extend(repositories)
        
        # Check if there's a link to the next page in the response headers
        link_header = response.headers.get('Link')
        if link_header:
            # Extract the link to the next page from the header
            next_url = None
            for link in link_header.split(','):
                parts = link.split(';')
                if len(parts) == 2 and 'rel="next"' in parts[1]:
                    next_url = parts[0].strip()[1:-1]  # Remove angle brackets
                    break
            
            if next_url:
                url = next_url  # Update the URL for the next page
                params = {}     # Clear params to avoid duplication
            else:
                break  # No more pages, exit the loop
        else:
            break  # No link header found, exit the loop
    else:
        print(f"Error: {response.status_code}")
        break

# Now, you have all the repositories in the 'all_repositories' list
# You can process or display them as needed
for repo in all_repositories:
    print(repo['name'])
