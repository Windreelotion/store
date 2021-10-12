import xlwt
from YBfeil import select    # 执行命令时，请先修改 YBfeil文件包中的database的数据库名称

wb = xlwt.Workbook()

st = wb.add_sheet("t_employees")

sql = "select * from t_employees "
param = []
f = select(sql, param)
print(len(f[0]))
st.write(0, 0, "编号")
st.write(0, 1, "姓名")
st.write(0, 2, "职务")
st.write(0, 3, "上级编号")
st.write(0, 4, "出生时间")
st.write(0, 5, "工资")
st.write(0, 6, "comm")
st.write(0, 7, "部门编号")
for i in range(0, len(f)):
    for j in range(0, len(f[0])):
        st.write(i + 1, j, f[i][j])

wb.save("三国集团.xls")
