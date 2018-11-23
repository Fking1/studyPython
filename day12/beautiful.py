'''
    BeautifulSoup 的用法
    1.创建BeautifulSoup对象
    2.搜索节点 find_all find  find_all(name,attrs,string)   node.name  node.get_text() node['href']
    3.访问节点

'''

from bs4 import BeautifulSoup

url = '/home/fking/pythonContact/readhub.html'
html_doc = open(url,'r')  #获取文档内容字符串
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
print(soup.prettify())

links = soup.find_all('a')

# for link in links:
        # print(link.get('href'))
        # print(link)

    # print(link.get_text())