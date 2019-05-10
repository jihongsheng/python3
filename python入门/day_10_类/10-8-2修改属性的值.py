# -*- coding: UTF-8 -*-


class Car():
    """模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = "\n%s %s %s" % (str(self.year), self.make, self.model)
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("骑乘行驶了 %s 公里！" % str(self.odometer_reading))

    def update_odometer(self, mileage):  # 1
        """
        将历程表读数设置为特定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你不能把里程表倒回去！")

    def increment_odometer(self, miles):        # ❶
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


# #########################3.通过方法对属性的值进行递增
# 有时候需要将属性值递增特定的量，而不是将其设置为全新的值。假设我们购买了一辆二手车，且从购买到登记
# 期间增加了100英里的里程，下面的方法让我们能够传递这个增量，并相应地增加里程表读数：
my_new_car = Car(make='奥迪', model='a4', year=2015)      # ❷
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23500)       # ❸
my_new_car.read_odometer()

my_new_car.increment_odometer(100)      # ❹
my_new_car.read_odometer()

"""
在❶处，新增的方法increment_odometer() 接受一个单位为英里的数字，并将其加入到self.odometer_reading 中。
在❷处，我们创建了一辆二手车——my_used_car 。在❸处，我们调用方法update_odometer() 并传入23500 ，将这
辆二手车的里程表读数设置为23 500。在❹处，我们调用increment_odometer()并传入100 ，以增加从购买到登记期
间行驶的100英里：
"""
# 你可以轻松地修改这个方法，以禁止增量为负值，从而防止有人利用它来回拨里程表。
# 注意 　你可以使用类似于上面的方法来控制用户修改属性值（如里程表读数）的方式，但能够访问程序的人都可
# 以通过直接访问属性来将里程表修改为任何值。要确保安全，除了进行类似于前面的基本检查外，还需特别注意细节。

