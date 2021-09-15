print("欢迎来到骗死人不偿命的猜数字游戏")
import random
x = random.randint(0, 100)
金币 = 500
a = 0
while a < 3:
    y = int(input("请输入一个数字"))
    if y == x:
        print("恭喜你猜对了!!!")
        金币 = 金币+10
        print(金币)
        a = a
    else:
        print("恭喜你猜错了!!!")
        金币 = 金币-100
        print(金币)
        a = a+1
