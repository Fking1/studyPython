'''
    左闭右开
'''
# 1.按下标取字符串中的字符
s = 'Hello python'
print(s[0])

# 2.访问字符串的子串  切片操作
print(s[0:5])

# 3.字符串拼接
s1 = "hello"
s2 = " nihao"
s = s1+s2
print(s)

# 4.字符串的更新操作
'''
    分为两步  
    1.切片
    2.拼接
'''
s1 = "hello python"
s2 = "String"
print(s1[:6]+s2)

