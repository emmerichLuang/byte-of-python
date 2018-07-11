#!/usr/bin/env python
# -*- coding:utf-8 -*-
# encoding=utf-8
# @Desc: 
# @Author: E.E.
# @Email:emmerichliang@gmail.com 
# @Time : 2018/7/11 17:01


# Print("Hello World")

# ctrl+d 抛异常
# s = input('Enter something --> ')

try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))