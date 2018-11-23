'''
    列表 list 一组数据
    list是有序的序列
    可以存储多种数据类型
'''
list1 = ['建国','爱国','魏国']
print(type(list1))
print(list1)

list1 = ['建国',20,'爱国',18,'魏国',15]
print(list1)


# 访问列表
print(list1[0])
print(list1[2:])
print(list1[2:4])

# 更新列表
list1[1] = 14
print(list1)

# 添加操作
list1.append("建军")
list1.append(26)
print(list1)

list1+=['爱民',24]
print(list1)

# 删除操作
del list1[4]
print(list1)