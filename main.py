import os
from curl_cffi import requests as curl_requests

# Get the URL from the environment variable
# The input 'url' from the workflow will be available as GITHUB_INPUT_URL
target_url = os.getenv('GITHUB_INPUT_URL')
backend_webhook_url = os.getenv('GITHUB_INPUT_WEBHOOK_URL') # You'll pass this from GH Actions

if not target_url:
    print("Error: URL not provided. Please provide a URL via the workflow input.")
    exit(1) # Exit if no URL is provided

print(f"Scraping URL: {target_url}")

if not backend_webhook_url:
    print("Error: Backend webhook URL not provided. Please provide a webhook URL via the workflow input.")
    exit(1) # Exit if no webhook URL is provided

try:
    r = curl_requests.get(target_url, impersonate="chrome")
    scraped_html = r.text
    print(scraped_html[:1000])  # Print the first 1000 characters of the HTML content
    
    payload = {
        "source_url": target_url,
        "scraped_html": scraped_html
    }
    print(f"Sending results to backend: {backend_webhook_url}")
    response = curl_requests.post(backend_webhook_url, json=payload)
    response.raise_for_status()
    print("Scraping and sending results completed successfully.")
except Exception as e:
    print(f"An error occurred during scraping: {e}")
