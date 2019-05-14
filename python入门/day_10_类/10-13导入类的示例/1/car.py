# -*- coding: UTF-8 -*-
# 一个可用于表示汽车的类


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


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=85):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    # 方法describe_battery()也移到了这个类中
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("电瓶的容量是%sKWH毫安！" % str(self.battery_size))

    def get_range(self):
        """打印一条消息，之处电瓶的续航里程"""

        if self.battery_size == 70:
            ranges = 240

        elif self.battery_size == 85:
            ranges = 270

        message = "这辆车大概能开%s" % str(ranges)
        message += "充满电的英里数。"
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性，在初始化电动车特有属性"""
        super().__init__(make, model, year)
        self.battery = Battery()





