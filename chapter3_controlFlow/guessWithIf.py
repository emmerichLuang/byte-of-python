### Python 中不存在 switch 语句
### 只能用if。。。elif...else的写法
### 或者py特于的字典


answer = 111

# 谨记，这里只输入整形。异常什么的以后再说
guess = int(input("输入一个整形："))

if guess == answer :
    print("猜对了！，答案是", guess)
elif guess > answer:
    print("你猜得大了点~")
else :
    print("你猜得小了点~")

print("游戏结束！")

