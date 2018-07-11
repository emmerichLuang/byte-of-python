#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Desc: pickle库，持久化py对象
# @Author: E.E.
# @Email:emmerichliang@gmail.com 
# @Time : 2018/7/11 15:39

import pickle


# The name of the file where we will store the object
shoplistfile = 'shoplist.data'

# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')

# Dump the object to a file
pickle.dump(shoplist, f)
f.close()

# Destroy the shoplist variable
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')

# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)