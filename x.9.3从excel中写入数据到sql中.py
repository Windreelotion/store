import xlrd
from YBfeil import update  # 执行命令时，请先修改 YBfeil文件包中的database的数据库名称


wb = xlrd.open_workbook(filename=r"E:\Python学习\day9\2020年每个月的销售情况.xlsx", encoding_override=True)

names = wb.sheet_names()
a = 0
for i in names:
    sheet = wb.sheet_by_name(i)  # 执行表
    rows = sheet.nrows  # 多少行
    cols = sheet.ncols  # 多少列
    a = a+1
    for q in range(1, rows):
        date = sheet.row_values(q)  # date为从第2行到行尾
        sql = f"insert into sale{a} values (%s,%s,%s,%s,%s)"  # sql语句，在sale中创建%,%,%,%,% 模糊数据
        param = [date[0], date[1], date[2], date[3], date[4]]
        update(sql, param)
