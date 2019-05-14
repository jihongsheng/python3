# -*- coding: UTF-8 -*-


class Car():
    """一次可用于表示汽车的类"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = "%s %s %s" % (self.year, self.make, self.model)
        return long_name.title()

    def read_odometer(self):
        """打印一条消息，之处汽车的里程"""
        print("骑乘行驶了 %s 公里！" % str(self.odometer_reading))

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值
        拒绝将里程往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你不能把里程表倒回去！")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
