# 本次循环结束，开始下一次循环

answer = 23

while True:
    iInput = int(input("请输入一个整形:"))

    if iInput == answer:
        print("猜对了！，答案是", iInput)
    elif iInput > answer:
        print("你猜得大了点~")
        continue
    else:
        print("你猜得小了点~")
        continue
    break

