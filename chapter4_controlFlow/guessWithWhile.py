answer = 111

running = True

while running :
    guess = int(input("输入一个整形："))

    if guess == answer:
        print("猜对了！，答案是", guess)
        running = False
    elif guess > answer:
        print("你猜得大了点~")
    else:
        print("你猜得小了点~")
else:
    print("这是while的else块。while结束就到这里")

print("游戏结束")

