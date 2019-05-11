# -*- coding: UTF-8 -*-
class Car():        # ❶
    """一次模拟汽车的简单尝试"""

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

    def update_odometer(self, mileage):
        """
        将历程表读数设置为特定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你不能把里程表倒回去！")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """表示汽车的各个方面，具体到电动汽车。"""

    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，在初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("这辆车有 %s KWH电池！" % str(self.battery_size))


my_tesla = ElectricCar(make='特斯拉', model='model s', year=2016)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()


