import requests
from bs4 import BeautifulSoup

url = 'https://readhub.cn/topics'
response = requests.get(url)

soup = BeautifulSoup(response.text,'lxml')
print(soup.xpath())
# print(soup.select('#itemList > div.topicItem___3YVLI.detail___3e_fy.selected___12Hz5 > h2 > a'))
