用户名 = 'root'
密码 = 'admin'
C = 0
print(f'用户名:{用户名}')
while C < 3:
    C = C + 1
    B = input("密码:")
    if B == 密码:
        print("密码正确!!!")
        break
    if C == 3:
        print("密码错误三次，已自动锁定")
        continue
    print("密码错误!!!")