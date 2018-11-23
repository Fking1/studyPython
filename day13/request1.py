import requests

url = 'https://www.baidu.com'
url2 = 'https://api.github.com/user'
url3 = 'http://www.donews.com/news/detail/1/3028688.html'
# 用urllib相关发送请求
# r = urllib.request.urlopen(url)
# print(r.status)
# print(r.headers)


# 使用requests发送请求  并且认证登录
# r = requests.get(url2, auth=('FKing1','fang12345698'))
# print(r.status_code)
# print(r.text)
# print(r.headers['Content-Encoding'])
# print(r.headers['Content-Type'])
# print(r.headers['Date'])


# 带参数的请求   改变github账户信息
# r = requests.patch(url2, auth=('FKing1','fang12345698'),json={'name': 'fking','blog':'fangqcloud.club','location':'广东省东莞市松山湖'})
# print(r.text)
# print(r.headers)
# print(r.status_code)


# 爬取新闻网站内容
# r = requests.get(url3)
# print(r.text)


# 自动下载图片
def download_image():
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1542900245980&di=2fadc8ed809650e504ea4d7951a14add&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180607%2F28ecf285639549c0b68567bab3e3463b.jpeg'
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    response = requests.get(url,headers=headers,stream=True)
    # print(response.status_code)
    # print(response.headers)
    with open('demo.jpg','wb') as fd:
        # 每128字节写入一次
        for chunk in response.iter_content(128):
            fd.write(chunk)
download_image()

def download_image_improved():
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1542900245980&di=2fadc8ed809650e504ea4d7951a14add&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180607%2F28ecf285639549c0b68567bab3e3463b.jpeg'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    from contextlib import closing
    with closing(requests.get(url,headers,stream=True)) as response:
        with open('demo1.jpg','wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)
download_image_improved()