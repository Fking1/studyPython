# 正则表达式
# re 是python正则表达式库 使用前需要导入
# findall 匹配所有
# search 匹配第一个
# match 只匹配开头的 re.I忽略大小写
import re
string = "hellow76472orld123@～qq1.comh23efan方llo"
reg = "hello"
result = re.findall(reg,string)
print(result)

# 常用的元字符
'''
    . 匹配除换行符以外的所有字符
    \w 匹配单词(包括中文)
    \s 匹配space 空白
    \d 匹配数字
    \b 匹配单词为边界(以单词开头或结尾)
    ^ 匹配字符串的开始
    $ 匹配字符串的结束
    \W \S \D均表示相反
    [^abcd] 匹配除了abcd以外的所有字符
    * 重复0次或多次
    + 重复1次或多次
    ? 重复0次或1次
    {n} 重复n次
    {n,m} 重复n~m次
    {n,} 重复n次及以上
    
'''
reg = "\d"
result = re.findall(reg,string)
print(result)


reg = "^hello"
result = re.findall(reg,string)
print(result)

reg = "hello$"
result = re.findall(reg,string)
print(result)

reg = "\w"
result = re.findall(reg,string)
print(result)

reg = "\W"
result = re.findall(reg,string)
print(result)

reg = "\d{2,}"
result = re.findall(reg,string)
print(result)

# 组匹配
string = 'this is my phone:13888888888 and this is my postcode:012345'
reg = "this is my phone:(\d{11}) and this is my postcode:(\d{6})"
result = re.search(reg,string).group(0)
print(result)
result = re.search(reg,string).group(1)
print(result)
result = re.search(reg,string).group(2)
print(result)

string = "hellopythonHello"
reg = "hello"
result = re.match(reg,string).group()
print(result)

string = "HellopythonHello"
reg = "hello"
result = re.match(reg,string,re.I).group()
print(result)
