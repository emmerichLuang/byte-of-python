# py的函数重载
# 只有那些位于参数列表末尾的参数才能被赋予默认参数值

def say_hello(msg, times=1):
    print(msg*times)


say_hello("不早啦")

say_hello("很晚啦！", 10)

