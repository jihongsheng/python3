# -*- coding: UTF-8 -*-
from car import Car


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

