A = 0
B = '* '
C = ' '

while A < 7:
    D = (C * (6 - A)) + (B * A) + (C * (5 - A))
    A = A + 1
    if D == '* * * * * * *':
        print(D)
        break
    else:
        D != '* * * * * * *'
        print(D)


S = int(input("\n请输入你想构建的层数:"))
a = 0
b = '* '
c = ' '
e = 2 * S - 1
while True:
    a = a + 1
    d = c * (e - a) + b * a + c * (e - a)
    if a == S:
        print(d)
        break
    else:
        a != S
        print(d)

