import sys
## sys 模块包含了与 Python 解释器及其环境相关的功能，也就是所谓的系统功能（system）
print('sys的args：')

for i in sys.argv:
    print(i)

print('sys path：', sys.path)

## 外面调用这个脚本

##E:\python_workspace\简明py\chapter6_module>python using_sys.py we are args
##sys的args：
##using_sys.py
##we
##are
##args
##sys path： ['E:\\python_workspace\\简明py\\chapter6_module', 'D:\\python3\\pytho
##n35.zip', 'D:\\python3\\DLLs', 'D:\\python3\\lib', 'D:\\python3', 'D:\\python3\\
##lib\\site-packages']
