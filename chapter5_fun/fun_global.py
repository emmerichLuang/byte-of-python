# 引用全局变量，不需要global声明，修改全局变量，需要使用global声明

k = 100


def func():
    global k

    print("val:", k)
    k = 1111
    print("after val:", k)


func()

print("finally value:", k)

