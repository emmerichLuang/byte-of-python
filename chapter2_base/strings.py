# 单引号/双引号
# 特殊符号原样输出

string1 = '原样输出\t23333'
print(string1)
string2 = '原样输出\t23333'
print(string2)

# 三引号可以指定多行
string3 = '''这是一段多行字符串。这是它的第一行。
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
print(string3)

# 字符串不可变？
# 赋值新建
strChange = "内容1"
print(strChange)
strChange = "内容2"
print(strChange)

