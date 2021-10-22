from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from 工商银行完整版 import bank_addUser
from 工商银行完整版 import bank_takeMoney
from 工商银行完整版 import bank_saveMoney
from 工商银行完整版 import bank_transformMoney

# 测试开户功能
da = [
    ["boy", "123456", "中国", "湖北省", "武汉市", "s001", 5000, 1],
    ["boy", "123456", "中国", "湖北省", "武汉市", "s001", 5000, 2],
    ["boys", "123456", "中国", "湖北省", "武汉市", "s001", 5000, 3],
]


@ddt
class TestBank(TestCase):
    for i in range(97):
        name = "boy" + str(i)
        bank_addUser(name, "123456", "中国", "湖北省", "武汉市", "s001", 5000)

    @data(*da)
    @unpack
    def testAddUse(self, a, b, c, d, e, f, g, h):
        s = bank_addUser(a, b, c, d, e, f, g)

        self.assertEqual(h, s)


# 测试存钱功能
da2 = [
    ['PpoOkC6z', 4000, True],
    ['PpoOkC6z1', 4000, False],
    ['PpoOkC6z', -1000, 2]
]


@ddt
class saveMoney(TestCase):
    @data(*da2)
    @unpack
    def testmoney(self, a, b, c):
        s = bank_saveMoney(a, b)

        self.assertEqual(c, s)


# 测试取钱功能
da1 = [
    ['PpoOkC6z', "654321", 4000, 0],
    ['PpoOkC6z1', "654321", 4000, 1],
    ["PpoOkC6z", "123456", 4000, 2],
    ["PpoOkC6z", "654321", 9000, 3],
    ["PpoOkC6z", "654321", -1000, 3]
]


@ddt
class draw(TestCase):
    @data(*da1)
    @unpack
    def testmoney(self, a, b, c, d):
        s = bank_takeMoney(a, b, c)

        self.assertEqual(d, s)


da3 = [
    ['PpoOkC6z', 'H6UvHHfp', '654321', 4000, 0],
    ['PpoOkC6', 'H6UvHHfp', '654321', 4000, 1],
    ['PpoOkC6z', 'H6UvHHf', '654321', 4000, 1],
    ['PpoOkC6z', 'H6UvHHfp', '65432', 4000, 2],
    ['PpoOkC6z', 'H6UvHHfp', '654321', 12000, 3],
    ['PpoOkC6z', 'H6UvHHfp', '654321', -1000, 3],
]


@ddt
class transform(TestCase):
    @data(*da3)
    @unpack
    def testmoney(self, a, b, c, d, e):
        s = bank_transformMoney(a, b, c, d)

        self.assertEqual(e, s)
