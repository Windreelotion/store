from threading import Thread
import time

basket = 0


class producer(Thread):
    name = ""
    counter = 0

    def run(self) -> None:
        global basket
        while True:
            if 50 > basket:
                basket = basket + 1
                print(self.name, "厨师向篮子丢入一个汉堡")
                self.counter += 1
            elif basket == 50:

                continue
            else:
                print(self.name, "厨师，做了", self.counter, "个")
                break


class consumer(Thread):
    name = ""
    balance = 100
    stop = 0

    def run(self) -> None:
        global basket
        while True:
            if self.balance > 0:
                self.balance -= 5
                basket -= 1
                print(self.name, "顾客吃了一个汉堡")
                if basket <= 0:
                    time.sleep(3)
                    self.stop += self.stop
                else:
                    continue
            else:
                print("篮子空了", self.stop, "次")
                break


p1 = producer()
p1.name = "1号"
p2 = producer()
p2.name = "2号"
p3 = producer()
p3.name = "3号"

m1 = consumer()
m1.name = "1号"
m2 = consumer()
m2.name = "2号"
m3 = consumer()
m3.name = "3号"
m4 = consumer()
m4.name = "4号"
m5 = consumer()
m5.name = "5号"
m6 = consumer()
m6.name = "6号"

p1.start()

m1.start()
m2.start()
m3.start()
m4.start()
m5.start()
m6.start()
p2.start()
p3.start()