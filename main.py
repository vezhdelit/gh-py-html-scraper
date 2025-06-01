import os
from curl_cffi import requests as curl_requests

# Get the URL from the environment variable
# The input 'url' from the workflow will be available as GITHUB_INPUT_URL
target_url = os.getenv('GITHUB_INPUT_URL')

if not target_url:
    print("Error: URL not provided. Please provide a URL via the workflow input.")
    exit(1) # Exit if no URL is provided

print(f"Scraping URL: {target_url}")

try:
    r = curl_requests.get(target_url, impersonate="chrome")
    html = r.text
    print(html[:1000])  # Print the first 1000 characters of the HTML content
except Exception as e:
    print(f"An error occurred during scraping: {e}")
