# 字典是一种可变容器类型 也是可以存储任意类型的对象
# 类似于java中的map

d = {'建国':12,'卫国':20,'爱国':25}
print(d)

# 获取所有key 或 value
keys = d.keys()
values = d.values()
print(keys)
print(values)

# 访问value值
print(d['建国'])

# 增加
d['小明'] = 12

# 更新
d['建国'] = 20

# 删除
del d['卫国']

print(d)

# 键是否在字典中
i = '卫国' in d
j = '建国' in d
k = '建国' not in d
print(i)
print(j)
print(k)