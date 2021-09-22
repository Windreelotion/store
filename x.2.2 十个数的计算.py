# 第二题
a = 1
c = 0
d = 0
while a <= 10:
        b = int(input(f"请输入第{a}数字"))
        a = a + 1
        c = c + b
        if d < b:
            d = b
print(f'10个数之和为:{d}')
print(f'输入的10个数的最大值:{c}')
print(f'平均值为:{c/10}')
