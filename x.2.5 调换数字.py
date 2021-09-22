A = 56
B = 77
C = 0
S = 9
D = '+'
E = '-'
print(f'A={A}')
print(f'B={B}')
while True:
    C = input("请输入+或者-使A和B调换:")
    S = B
    B = A
    A = S
    if C == D or C == E:
        print(f'A={A}')
        print(f'B={B}')
        break
