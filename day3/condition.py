'''
    比较运算符 == ：比较两个变量的值是否相等
    注意在Python中代码的缩进很重要
'''
# 1
condition = True
if condition:
    print("条件为真")

# 2
condition = False
if condition:
    print("条件为真")
else:
    print("条件为假")

# 3
condition = 4
if condition<3:
    print("条件小于3")
elif condition<5:
    print("条件在3~5")
else:
    print("条件大于等于5")
