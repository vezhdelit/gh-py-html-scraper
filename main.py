from curl_cffi import requests as curl_requests

target_url = 'https://hard.rozetka.com.ua/ua/patriot_p300p512gm28/p187100593/'
r = curl_requests.get(target_url, impersonate="chrome")
html = r.text
print(html[:1000])  # Print the first 1000 characters of the HTML content
