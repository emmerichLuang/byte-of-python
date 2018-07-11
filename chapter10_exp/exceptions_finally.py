#!/usr/bin/env python
# -*- coding:utf-8 -*-
# encoding=utf-8
# @Desc: 
# @Author: E.E.
# @Email:emmerichliang@gmail.com 
# @Time : 2018/7/11 17:09

import sys
import time

f = None

try:
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        # 为了确保它能运行一段时间
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")