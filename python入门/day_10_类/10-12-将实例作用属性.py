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


# 我们定义了一个名为Battery 的新类，它没有继承任何类
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    # 方法__init__() 除self 外，还有另一个形参battery_size 。这个形参是可选的：如果没有给
    # 它提供值，电瓶容量将被设置为70。
    def __init__(self, battery_size=85):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    # 方法describe_battery()也移到了这个类中
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("电瓶的容量是%sKWH毫安！" % str(self.battery_size))

    def get_range(self):
        """打印一条消息，之处电瓶的续航里程"""

        # 处新增的方法get_range() 做了一些简单的分析：如果电瓶的容量为70kWh，
        # 它就将续航里程设置为240英里；
        if self.battery_size == 70:
            range= 240
        # 如果容量为85kWh，就将续航里程设置为270英里，然后报告这个值。
        elif self.battery_size == 85:
            range = 270

        message = "这辆车大概能开%s" % str(range)
        message += "充满电的英里数。"
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性，在初始化电动车特有属性"""
        super().__init__(make, model, year)
        # 在ElectricCar 类中，我们添加了一个名为self.battery 的属性
        self.battery = Battery()
        # 这行代码让Python创建一个新的Battery 实例（由于没有指定尺寸，因此为默认值70 ），并将
        # 该实例存储在属性self.battery 中。每当方法__init__() 被调用时，都将执行该操作；因此
        # 现在每个ElectricCar 实例都包含一个自动创建的Battery 实例。


my_tesla = ElectricCar(make='特斯拉', model='model s', year=2016)

print(my_tesla.get_descriptive_name())
# 我们创建一辆电动汽车，并将其存储在变量my_tesla 中。要描述电瓶时，需要使用电动汽车的属性battery ：
my_tesla.battery.describe_battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# 为使用这个方法，我们也通过汽车的属性battery 来调用它
my_tesla.battery.get_range()
