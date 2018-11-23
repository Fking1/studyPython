'''
    python注释的另一种方式
'''
# 将十进制转换成二进制
i = 16
j = bin(i)
print(j)

# 将十进制转换成八进制
i = 16
j = oct(i)
print(j)

# 将十进制转换成十六进制
i = 16
j = hex(i)
print(j)

# 二进制转换成十进制  不可直接i=10
i= '10'
j = int(i,2)
print(j)

# 八进制转换成十进制
i = '10'
j = int(i,8)
print(j)

# 十六进制转换成十进制
i = '10'
j = int(i,16)
print(j)
