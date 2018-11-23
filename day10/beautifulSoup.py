'''
    一个可以从html/xml文件中提取数据的一个python库
    pip install beautifulsoup4 安装beautifulsoup
    open(文件地址,权限,encoding="字符集")
'''
import re
from bs4 import BeautifulSoup

html_doc = "/home/fking/pythonContact/readhub.html" #html文件地址/路径
html_doc2 = 'http://www.donews.com/news/detail/4/3028687.html'
html_file = open(html_doc,"r") #文件地址，权限
html_handle = html_file.read()

soup = BeautifulSoup(html_handle,'html.parser')
# print(soup)

# print(soup.head)  #获取文档头

# print(soup.p)  #获取p标签

# print(soup.p.attrs) #取第一个p标签的属性

# print(soup.find_all("p"))

# a = "layout___30l4Y"
# print(soup.find_all(id = a))

result = soup.find_all("div",class_="bp-pure___3xB_W")
print(result)

content = soup.find_all("div",class_="bp-pure___3xB_W")
reg = ">(.{1,})</div>"
result = re.findall(reg,str(content))
print(result)
