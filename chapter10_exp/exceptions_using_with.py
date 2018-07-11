#!/usr/bin/env python
# -*- coding:utf-8 -*-
# encoding=utf-8
# @Desc: 不用finally close
# @Author: E.E.
# @Email:emmerichliang@gmail.com 
# @Time : 2018/7/11 17:18


with open("poem.txt") as f:
    for line in f:
        print(line, end='')