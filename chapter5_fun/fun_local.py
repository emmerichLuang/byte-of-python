
# 局部变量修改是没用的

x = 100


def func(x):

    print("val:", x)
    x = 1111
    print("after x val:", x)


func(x)

print("finally x value:",x)

