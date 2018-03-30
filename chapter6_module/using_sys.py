import sys


print('命令行参数：')

for i in sys.argv:
    print(i)

print('环境变量：',sys.path)



'''
E:\py_workspace\byte-of-python\chapter6_module>python using_sys.py  canshu
命令行参数：
using_sys.py
canshu
环境变量： ['E:\\py_workspace\\byte-of-python\\chapter6_module', 'D:\\Program Fi
les\\python36\\python36.zip', 'D:\\Program Files\\python36\\DLLs', 'D:\\Program
Files\\python36\\lib', 'D:\\Program Files\\python36', 'D:\\Program Files\\python
36\\lib\\site-packages']
'''