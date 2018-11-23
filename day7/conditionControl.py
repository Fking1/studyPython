'''
    条件控制
    1、比较运算符
    ==
    >
    <
    >=
    <=
    !=

    不仅数字可以比较 字符也可以相互比较
    ord()获取相应的ASCII值
    chr()是ord()的互逆操作
'''

# i = 'a'
# j = 'b'
# if i>j:
#     print("a>b")
# else:
#     print("a<b")
#
# print(ord(i))
# print(ord(j))
# print(ord('A'))



'''
    2.成员运算符
    1.in 
    2.not in
'''

'''
    3.逻辑运算符
    and or not
'''
person = ['爱国','卫国','建国','国庆','建军']
if '爱国' in person and '建国' in person:
    print("爱国 建国都在房子里")

'''
    身份运算符id()取变量的地址
    is 判断地址是否相等 == 直接判断值是否相等
    is not
'''
i = 1
j = 1
print(i == j)
print(i is j)
print(id(i))
print(id(j))

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)
print(list1 == list2)
print(id(list1))
print(id(list2))