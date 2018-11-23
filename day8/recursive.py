'''
    递归函数
    明确递归结束的条件
    优点：写法简洁
    缺点：效率不高
'''

# 死递归
# def my_function(x):
#     print(x)
#     my_function(x+1)
#
# my_function(1)

# 阶乘计算

def jiechen_func(x):
    if(x==1):
        return x
    else:
        return x*jiechen_func(x-1)


result = jiechen_func(5)
print(result)

'''
    __name__
'''

def my_func():
    print(__name__)

my_func()

if __name__ == "__main__":
    print("这是函数的入口")