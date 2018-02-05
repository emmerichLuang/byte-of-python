# 强制中断循环。不管你几层循环。 else块也不会执行

answer = 23
while True:
    iInput = int(input("请输入一个整形:"))

    if iInput == answer:
        print("猜对了！，答案是", iInput)
        break
    elif iInput > answer:
        print("你猜得大了点~")
    else:
        print("你猜得小了点~")
else:
    print("这是while的else块。除非break掉，while结束会到这里")

print("游戏结束！")