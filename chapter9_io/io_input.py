#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Desc: input()函数， 在命令提示行中， 输入字符串
# @Author: E.E.
# @Email:emmerichliang@gmail.com 
# @Time : 2018/6/22 17:12


# 负数步长，返回翻转的文本
def reverse(text):
    return text[::-1];


def is_palindrome(text):
    if text == reverse(text):
        return True;
    else:
        return False;


something = input("Enter text: ")

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")