#!/usr/bin/env python
# -*- coding:utf-8 -*-
# encoding=utf-8
# @Desc: 输出中文不乱码
# @Author: E.E.
# @Email:emmerichliang@gmail.com 
# @Time : 2018/7/11 16:39


import io
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"说点中文")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)

