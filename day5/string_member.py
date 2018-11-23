'''
    python3 -m pydoc -p 8888
'''

# 字符串的成员运算
s1 = "hello python"
s2 = "h"

# 包含运算 in
print(s2 in s1)

# 不包含运算 not in
print(s2 not in s1)

# 转义字符 \
print("\'")

# 换行符 \n

# 字表符 \t

# %s 替换字符串

# %d 替换整形
print("我叫%s 今天是我第%d天学习python" %('方勇',5))


# 字符串的内建函数

s = 'Hello Python'

# 1.查找字符串  find(char)  返回第一个位置
print(s.find("l"))

# 2.转换成小写字符
print(s.lower())

# 3.转换成大写字符
print(s.upper())

# 4.字符串替换
print(s.replace("o","ee"))