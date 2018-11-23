# 贪婪与非贪婪
'''
    贪婪代表了尽可能多的匹配
    非贪婪代表尽可能少的匹配
    默认贪婪
    非贪婪符: ?
    用在 * + ? 后面的，要求匹配越少越好
'''
import re
string = "helloworldpythonhello"
reg = 'hello*'
result = re.findall(reg,string)
print(result)

reg = 'hello*?'
result = re.findall(reg,string)
print(result)

reg = 'hello+?'
result = re.findall(reg,string)
print(result)

reg = 'hello??'
result = re.findall(reg,string)
print(result)