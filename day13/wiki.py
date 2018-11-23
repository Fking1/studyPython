from bs4 import BeautifulSoup
import requests
import re
url = 'https://baike.baidu.com/'
html_doc = requests.get(url,allow_redirects=False)

print(html_doc.text)
# soup = BeautifulSoup(html_doc,'html.parser')
# print(soup)