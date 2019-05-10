# -*- coding: UTF-8 -*-
# 类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法__init__()
# 内指定这种初始值是可行的；如果你对某个属性这样做了，就无需包含为它提供初始值的形参。
# 下面来添加一个名为odometer_reading 的属性，其初始值总是为0。我们还添加了一个名为read_odometer() 的方法
# ，用于读取汽车的里程表：


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
        long_name = "%s %s %s" % (str(self.year), self.make, self.model)
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("骑乘行驶了 %s 公里！" % str(self.odometer_reading))


my_new_car = Car(make='奥迪', model='a4', year=2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


"""
python创建了一个名为odometer_reading的属性，并将其初始值设置为0.还定义了一个read_odometer方法，他让你
能轻松的获得启程历程
一开始汽车里程为0
出售时历程读数为0的汽车并不多，因此我们需要修改属性的值的途径
"""
