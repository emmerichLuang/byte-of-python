# 字符串格式化 下标从0开始
yourName = 'Emmerich'
print("Hello~ what's your name? \nMy name is {0}".format(yourName))
# +号拼字符串
print("Great! " + yourName  + " is a good name~")

# 不需要行号
print("I do think {} is a good name,too~ HaHa~.".format(yourName))

# 保留2位小数
print("{0:.2f}".format(1.0/3))

# 填充
# 填充下划线_；内容居中；字符串长度11.
print('{0:_^11}'.format('hello'))

# 关键词填充
print("Hi all! My name is {name}. I am a {job}.".format(name='Emmerich',job="codeTyper"))

# print 默认是换行的。 下面的方式可以不换行
# 同理，end=' ' 最后就是空格
print("不换行的做法。",end='')
print("看！没换行了吧？",end=' 23333')

