import sys

# 内置的 dir() 函数能够返回由对象所定义的名称列表

print(dir(sys))

# 如果没有提供参数，函数将返回当前模块的名称列表。
a = 5
print(dir())

del a
print(dir())