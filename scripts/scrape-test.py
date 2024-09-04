import requests_html
# import json

url = "https://tw.yahoo.com/"
session = requests_html.HTMLSession()

# 设置自定义 User-Agent 头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://news.pts.org.tw/'
}

response = session.get(url, headers=headers)
print(response.status_code)