print("输入a,b,c三条边，看看是否能组成三角形")
a = float(input('请输入a的边长:'))
b = float(input('请输入b的边长:'))
c = float(input('请输入c的边长:'))
z = a+b
aa = a*a
bb = b*b
cc = c*c
x = a+c
y = b+c
if z <= c or x <= b or y <= a:
    print("不能组成三角形")
else:
    if a == b == c:
        print("可以组成等边三角形")
    else:
        if a == b or a == c or b == c:
            print("可以组成等腰三角形")
    if z > c and x > b and y > a and z != x and x != y and aa == bb+cc:
        print("可以组成普通三角形")
    if aa == bb+cc or bb == aa+cc or cc == aa+bb:
        print("可以组成直角三角形")
