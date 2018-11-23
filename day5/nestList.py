# 嵌套列表 多重列表
list1 = [['建国','爱国','卫国'],[12,14,16]]
print(list1)

print(list1[0][1])

# 返回列表元素个数
print(len(list1))

# 移除一个元素 返回移除的元素内容
l = list1[0].pop(1)
print(l)
print(list1)

# 列表排序
list2 = [14,12,30,25,24]
list2.sort()
print(list2)

# 查看列表元素的索引
print(list2.index(12))