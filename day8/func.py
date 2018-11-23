'''
    函数定义的格式
'''
# 1.无参函数
def no_param_function():
    print("这是一个无参函数")

no_param_function()

# 2.有参函数
def param_function(a,b,c):
    print("这是一个有参函数，参数分别为:",a,b,c)

param_function("参数1","参数2",20)

# 3.默认参数
def default_param_function(name="狗蛋",sex="man",age=50):
    print("name="+name+"\nsex="+sex+"\nage="+str(age))

default_param_function("fang","woman",60)

# 4.参数混合函数
def mix_function(name,age=50):
    print(name,age)

mix_function("fang")

# 5.函数无返回值
def function_without_return():
    print("函数被调用")

p = function_without_return()
print(p)
print(type(p))

# 6.函数有一个返回值
def function_with_return_single(p):
    return p

x = function_with_return_single('fking')
print(x)
print(type(x))

# 7.函数有多个返回值
def function_with_return_multiple(name,age):
    print(name,age)
    return name,age

name1,age1 = function_with_return_multiple('fking',20)
print(name1,age1)

# 8.返回一个函数
def function_return_function(x):
    if x==2:
        def inner_func(y):
            return y*y

    if x==3:
        def inner_func(y):
            return y*y*y

    return inner_func

cal = function_return_function(3)
print(cal(4))