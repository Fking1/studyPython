import requests
import urllib3

# response1 = requests.get('https://www.baidu.com')
# print(response1.content)

http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
print(r)