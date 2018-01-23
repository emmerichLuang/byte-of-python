# 很常用的方式了

# 转义了 双引号包括单引号
print("What's your name?")

# 斜杠
print('What\'s your name?')

# 常见转义字符，惯例了：
# \t table
# \n 换行

# 末尾的反斜杠表示字符串将在下一行继续
longStr ="这是一段很长很长很长很长很长\
很长很长很长很长很长的文字"
print(longStr)

# 原始字符串（Raw）。显式输出转义字符
rStr = r'这是原始字符串，我想显示转义字符。\t以后你爱干嘛就干嘛\n'
print(rStr)

