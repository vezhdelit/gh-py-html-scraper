import os
from seleniumbase import SB
from curl_cffi import requests as curl_requests

target_url = os.getenv('GITHUB_INPUT_URL')
backend_webhook_url = os.getenv('GITHUB_INPUT_WEBHOOK_URL') 
# target_url = 'https://gitlab.com/users/sign_in'
# backend_webhook_url = 'https://nextjs-puppeteer-webscraper.vercel.app/api/webhook/scraped-html'

if not target_url:
    print("Error: URL not provided. Please provide a URL via the workflow input.")
    exit(1) # Exit if no URL is provided

print(f"Scraping URL: {target_url}")

if not backend_webhook_url:
    print("Error: Backend webhook URL not provided. Please provide a webhook URL via the workflow input.")
    exit(1) # Exit if no webhook URL is provided

try:
    with SB(uc=True, test=True) as sb:
        # sb.open(target_url)
        sb.activate_cdp_mode(target_url)
        sb.uc_gui_click_captcha()
        sb.sleep(2)
        sb.uc_gui_handle_captcha()
        scraped_html = sb.get_page_source()
        print(scraped_html[:1000])

        payload = {
            "source_url": target_url,
            "scraped_html": scraped_html
        }
        print(f"Sending results to backend: {backend_webhook_url}")
        response = curl_requests.post(backend_webhook_url, json=payload)
        response.raise_for_status()
        print("Scraping and sending results completed successfully.")
except Exception as e:
    print(f"An error occurred during SB scraping: {e}")
