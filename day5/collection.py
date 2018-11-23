'''
    集合是一个无序、不重复元素的序列
'''
# 声明一个集合 {}或者set()
set_param = {"钩子","嘎子","颖儿","钩子","秀儿"}
print(set_param)

print("狗子" in set_param)
print("嘎子" in set_param)

a = set("abcdef")
b = set("abcxyz")
print(a)
print(b)
# 与或非
print(a & b)
print(a | b)
print(a ^ b)

# 集合添加add() 集合移除remove()

# 随机移除pop()
pop_param = set_param.pop()
print(pop_param)