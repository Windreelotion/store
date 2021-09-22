a = [1, 5, 21, 30, 15, 9, 30, 24]
# 第一种方法:
i = 0
b = []
c = 0
while True:
    if i == len(a):
        break
    c = a[i]
    i = i + 1
    if c % 5 == 0:
        b.append(c)
    if c % 5 != 0:
        continue
print(f"为5的倍数的和:{sum(b)}")

# 第二种方法:
sum1 = 0
for aa in a:
    if aa % 5 == 0:
        sum1 = sum1 + aa
print(f"\n为5的倍数的和:{sum1}")
