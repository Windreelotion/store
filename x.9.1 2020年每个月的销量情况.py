import xlrd

# 导入Excel表
wb = xlrd.open_workbook(filename=r"E:\Python学习\day9\2020年每个月的销售情况.xlsx", encoding_override=True)

names = wb.sheet_names()  # 导出所有表的名字

# 1.全年的销售总额     = 价格 X 销售量
xse = 0

for i in names:
    sheet = wb.sheet_by_name(i)  # 表的名字挨个进行
    rows = sheet.nrows  # 行的数量
    xs = sheet.col_values(2)  # 表中销售价格xs
    sl = sheet.col_values(4)  # 表中销售数量sl
    sum1 = 0
    for j in range(1, rows):  # 循环 从 1 到 行的数量
        sum1 += xs[j] * sl[j]  # sum1 = 价格 X 数量
    xse += sum1  # 总销售额xse = xse + sum1

print(f"\n全年的销售总额为:" '%.1f' % xse)

# 2.每件衣服的销售(件数)占比     = 每件衣服的销售量 % 总销售量
print('-' * 60)  # 输出 ---X60个
zxsl = 0
yfzl = []
for i in names:  # 循环完列表名
    sheet = wb.sheet_by_name(i)  # 表的名字挨个进行
    yfmz = sheet.col_values(1)  # 表中衣服种类
    for j in range(1, sheet.nrows):
        yfzl.append(yfmz[j])  # 表中衣服种类

    zl = set(yfzl)  # 种类 = 衣服种类
    zl = list(zl)  # 种类列表 = 种类
print(zl)  # 衣服的种类

for i in names:  # 循环完列表名
    sheet = wb.sheet_by_name(i)  # 表的名字挨个进行
    xsl = sheet.col_values(4)  # 表中销售量
    for j in range(1, sheet.nrows):
        zxsl += xsl[j]  # 总销售量 = 总销售量 + 销售量
# print("衣服的总销售数量:",zxsl)  # 衣服的总销售数量


for q in zl:  # 循环完 种类 zl列表中的衣服名字
    mzsl = 0  # 衣服销售额 = 0
    for i in names:  # 循环完列表名
        sheet = wb.sheet_by_name(i)  # 表的名字挨个进行
        for j in range(1, sheet.nrows):  # 循环列表1-列表行，J = 第j行
            row = sheet.row_values(j)  # row行 = 表中的第j行
            if q == row[1]:  # 如果 q = 衣服种类
                mzsl += row[4]  # 每种销售额 = 每种销售额 + 销售量

            else:
                continue
    xszb = mzsl * 100 / zxsl
    print(f'{q}的销售数量占比为：{xszb}% ')
# 3.每件衣服的月销售占比     每件衣服的月销售量*每件衣服的价格/每月的总销售额
print('-' * 60)  # 输出 ---X60个
for i in names:
    sheet = wb.sheet_by_name(i)
    每月服装名称 = {}
    xsze = 0
    print(i, "的月销售占比:")
    for q in range(1, sheet.nrows):
        date = sheet.row_values(q)
        xsze += date[2] * date[4]
        if date[1] in 每月服装名称:
            每月服装名称[date[1]] = 每月服装名称[date[1]] + date[4] * date[2]
        else:
            每月服装名称[date[1]] = date[4] * date[2]
    for k in 每月服装名称:
        print("\t", k, ":", 每月服装名称[k] * 100 / xsze)

# 4.每件衣服的销售额占比   = 每种衣服销售额/总销售额
服装名称 = {}
print('-' * 60)  # 输出 ---X60个
for i in names:
    sheet = wb.sheet_by_name(i)
    for q in range(1, sheet.nrows):
        date = sheet.row_values(q)
        if date[1] in 服装名称:
            服装名称[date[1]] = 服装名称[date[1]] + date[4] * date[2]
        else:
            服装名称[date[1]] = date[4] * date[2]
for i in 服装名称:
    print(i, "的销售额占比", 服装名称[i] * 100 / xse)

# 5.最畅销的衣服是那种
print('-' * 60)  # 输出 ---X60个
服装名称 = {}
for i in names:
    sheet = wb.sheet_by_name(i)
    for q in range(1, sheet.nrows):
        date = sheet.row_values(q)
        if date[1] in 服装名称:
            服装名称[date[1]] = 服装名称[date[1]] + date[4]
        else:
            服装名称[date[1]] = date[4]
A = 0
a = 0

print(服装名称)
for k, v in 服装名称.items():
    if a == 0:
        A = k
        a = v
    elif a != 0:
        if a > v:
            continue
        else:
            A = k
            a = v

print("最畅销的衣服为:", A)

# 6.每个季度最畅销的衣服
print('-' * 60)  # 输出 ---X60个
names1 = [['3月', '4月', '5月'], ['6月', '7月', '8月'], ['9月', '10月', '11月'], ['12月', '1月', '2月']]
n = 0
for m in names1: # m循环names1的几个元素，从3,4,5到12,1,2
    季度衣服 = {}
    n = n +1
    for j in m:
        sheet = wb.sheet_by_name(j)
        for q in range(1, sheet.nrows):
            date = sheet.row_values(q)
            if date[1] in 季度衣服:
                季度衣服[date[1]] = 季度衣服[date[1]] + date[4]
            else:
                季度衣服[date[1]] = date[4]
    A = 0
    a = 0
    for k, v in 季度衣服.items():
        if a == 0:
            A = k
            a = v
        elif a != 0:
            if a > v:
                continue
            else:
                A = k
                a = v

    print("第",n,"季度畅销衣服为:",A)

# 7.全年销量最低的衣服
print('-' * 60)  # 输出 ---X60个
print(服装名称)
for k, v in 服装名称.items():
    if a == 0:
        A = k
        a = v
    elif a != 0:
        if a < v:
            continue
        else:
            A = k
            a = v
print("全年销量最低的衣服为:", A)
