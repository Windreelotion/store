import random
from YBfeil import update
from YBfeil import select


def welcome():
    print("========================")
    print("====欢迎使用北京工商银行====")
    print("====1.开户           ====")
    print("====2.取钱           ====")
    print("====3.存钱           ====")
    print("====4.转账           ====")
    print("====5.查询           ====")
    print("====6.退出系统        ====")
    print("========================")


bankname = "北京工商银行"
Bank = {}

myinfo = '''
    ------------账户信息------------
    账号：{account}
    姓名：{username}
    密码：{password}
    地址：
        国家：{country}
        省份：{province}
        街道：{street}
        门牌号：{door}
    账户余额：{money}
    银行名：{bankname}
    -------------------------------
'''


def panduan(account, username, password, country, province, street, door, money):
    sql1 = "select count(*) from bank"
    param = []
    data = select(sql1, param)

    if data[0][0] >= 100:
        return 3

    sql2 = "select * from bank where username = %s "
    param2 = [username]
    data2 = select(sql2, param2)

    if len(data2) != 0:
        return 2

    sql3 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
    param3 = [account, username, password, country, province, street, door, money, bankname]
    update(sql3, param3)
    return 1


def kh():
    print("使用开户功能成功")
    username = input("请输入用户名")
    password = input("请输入密码")
    print("下面请输入您的地址:")
    country = input("\t\t请输入您的国家:")
    province = input("\t\t请输入您的省份:")
    street = input("\t\t请输入您的街道:")
    door = input("\t\t请输入您的门牌号:")
    account = random.randint(10000000, 99999999)
    money = 0
    a = panduan(account, username, password, country, province, street, door, money)
    if a == 1:
        print("恭喜您开户成功，以下是您的开户信息:")
        print(myinfo.format(account=account,
                            username=username,
                            password=password,
                            country=country,
                            province=province,
                            street=street,
                            door=door,
                            money=money,
                            bankname=bankname
                            ))
    elif a == 2:
        print("该用户已经存在，请携带证件到其它银行办理开户，谢谢!")
    elif a == 3:
        print("银行账户库已满，请携带证件到其它银行办理，谢谢!")


def QQ():
    print("取钱功能:")
    zh = input("请输入账号")
    sql = "select * from bank where account = %s"
    parma = [zh]
    data = select(sql, parma)
    if len(data) != 0:
        mm = input("请输入密码")
        sql2 = "select * from bank where account = %s and password  = %s "
        parma2 = [zh, mm]
        data2 = select(sql2, parma2)
        print(data2)
        if len(data2) != 0:
            qq = int(input("请输入取钱的金额:"))
            if data2[0][7] >= qq:
                sql3 = "update bank set money = money-%s  where account = %s "
                parma3 = [qq, zh]
                update(sql3, parma3)
                sql9 = "select * from bank where account = %s and password  = %s "
                parma9 = [zh, mm]
                data9 = select(sql9, parma9)
                print("取钱成功!")
                print(f"您的剩余余额为:{data9[0][7]}")
            else:
                print("您的账户余额不足")
        else:
            print("输入密码错误，请重新输入")

    else:
        print("输入账号错误")


def CQ():
    print("存钱功能:")
    zh = input("请输入账号")
    sql = "select * from bank where account = %s"
    parma = [zh]
    data = select(sql, parma)
    if len(data) != 0:
        mm = input("请输入密码")
        sql2 = "select * from bank where account = %s and password  = %s "
        parma2 = [zh, mm]
        data2 = select(sql2, parma2)
        print(data2)
        if len(data2) != 0:
            cq = int(input("请输入存入的金额:"))
            sql3 = "update bank set money = money + %s where %s"
            parma3 = [cq, zh]
            update(sql3, parma3)
            sql9 = "select * from bank where account = %s and password  = %s "
            parma9 = [zh, mm]
            data9 = select(sql9, parma9)
            print("取钱成功!")
            print(f"您的剩余余额为:{data9[0][7]}")
        else:
            print("密码输入错误")
    else:
        print("账号输入错误")


def ZZ():
    print("转账功能:")
    zh = input("请输入账号")
    sql = "select * from bank where account = %s"
    parma = [zh]
    data = select(sql, parma)
    if len(data) != 0:
        mm = input("请输入密码")
        sql2 = "select * from bank where account = %s and password  = %s "
        parma2 = [zh, mm]
        data2 = select(sql2, parma2)
        print(data2)
        if len(data2) != 0:
            zz = input("请输入转账的账号:")
            sql3 = "select * from bank where account = %s"
            parma3 = [zz]
            data3 = select(sql3, parma3)
            if len(data3) != 0:
                zzq = int(input("请输入转账的金额"))
                sql4 = "select * from bank where money = %s "
                parma4 = []
                data4 = select(sql4, parma4)
                if data4[0][7] >= zzq:
                    sql5 = "update bank set money=moeny - %s where %s"
                    parma5 = [zzq, zh]
                    update(sql5, parma5)
                    sql9 = "select * from bank where account = %s and password  = %s "
                    parma9 = [zh, mm]
                    data9 = select(sql9, parma9)
                    print("取钱成功!")
                    print(f"您的剩余余额为:{data9[0][7]}")
                    sql6 = "update bank set money = money+ %s where %s"
                    parma6 = [zzq, zz]
                    update(sql6, parma6)
                else:
                    print("您的余额不足")
            else:
                print("输入转账的目标账号错误")
        else:
            print("输入密码错误")
    else:
        print("输入账号错误")


def CX():
    print("查询功能:")
    zh = input("请输入账号")
    sql = "select * from bank where account = %s"
    parma = [zh]
    data = select(sql, parma)
    if len(data) != 0:
        mm = input("请输入密码")
        sql2 = "select * from bank where account = %s and password  = %s "
        parma2 = [zh, mm]
        data2 = select(sql2, parma2)
        print(data2)
        if len(data2) != 0:
            sql3 = "select * from bank where money=%s"
            parma3 = []
            data3 = select(sql3, parma3)
            print("该账号的密码为:")
            print(data3[0][7])


welcome()
while True:
    q = input("请输入要使用的功能编号:")
    if q == '1':
        kh()
    elif q == '2':
        QQ()
    elif q == '3':
        CQ()
    elif q == '4':
        ZZ()
    elif q == '5':
        CX()
    elif q == '6':
        print("欢迎您下次使用本银行账户系统!")
        break
    else:
        print("胡乱输入,结束本次使用!")
        break
