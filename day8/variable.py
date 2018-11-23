'''
    变量的作用域
    1.在python中 无块级作用域
    在代码块中的变量  外部是可以调用的
    2.函数内部定义的变量 外部无法访问
    3.函数内部无法访问函数外部的变量
'''
# 1
if True:
    name = "尼古拉斯赵四"

print(name)

# 变量的作用域链 内层函数优先使用自己层级的变量 若无，则向外层寻找
def fun1():
    name="建国"

    def fun2():
        # name="卫国"
        print(name)
    fun2()
    print(name)

fun1()
