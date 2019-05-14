# -*- coding: UTF-8 -*-
# 对于父类方法，只要它不符合自雷模拟的实物的行为，都可以对其进行重写，为此，可在自雷中定义一个这样
# 的方法，即它与要重写的父类方法同名。这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的
# 相应方法。
# 假设Car 类有一个名为fill_gas_tank() 的方法，它对全电动汽车来说毫无意义，因此你可能想重写它。
# 下面演示了一种重写方式：


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

    def fill_gas_tank(self):
        """电动汽车没有油罐"""
        print("This car doesn't need a gas tank!")


make = ElectricCar('q', 'b', 2018)
print(make.get_descriptive_name())
make.read_odometer()
make.fill_gas_tank()

# 具体没看懂，后面研究
