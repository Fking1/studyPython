# requests库的使用
'''
    requests.get(url,param,headers)
    post
    delete
    put 均一致
'''
import requests

url = 'http://stockpage.10jqka.com.cn/600004/company/'

r = requests.get('https://api.github.com/events')
print(r.status_code)

r = requests.get(url)
print(r.url)
# print(r.text)

r = requests.get('https://api.github.com/events')
# print(r.text)
print(r.encoding)
# print(r.content)
# print(r.json())
print(r.headers)
print(r.headers.get('Content-Type'))