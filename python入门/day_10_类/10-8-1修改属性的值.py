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

    # def update_odometer(self, mileage):     # 1
    #     """将历程表读数设置为特定的值"""
    #     self.odometer_reading = mileage
    #

    def update_odometer(self, mileage):  # 1
        """
        将历程表读数设置为特定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:        # ❶
            self.odometer_reading = mileage
        else:
            print("你不能把里程表倒回去！")        # ❷


# 可以以三种不同方法修改属性的值：直接通过实例进行修改设置：听过方法进行递增（增加特定的值）
# ####################### 1. 直接修改属性的值
my_new_car = Car(make='aodi', model='a4', year=2016)
print(my_new_car.get_descriptive_name())

# 使用句点表示法来直接访问并设置属性odometer_reading。这行代码让python在实例my_new_car中找
# 到属性odometer_reading，并将该值属性的值设置为23
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# 有时候需要像这样直接访问属性，但其他时候需要编写对属性进行更新的方法

# ####################### 2. 通过方法修改属性的值
my_new_car = Car(make='aodi', model='a4', year=2016)
print(my_new_car.get_descriptive_name())

# 对Car类所做的唯一修改是在1处添加方法update_odometer().这个方法接受一个历程值，并将其存储到
# self.odometer_reading中。
# 这里调用update_odometer（）,并提供给实参25，它将里程碑读数设置为25，而方法read_odometer打印该读数
my_new_car.update_odometer(mileage=25)
my_new_car.read_odometer()

# 可对方法update_odometer()进行扩展，使其在修改里程表读数时做些额外工作，下面添加一些逻辑，禁止任何
# 人将里程表读数往回调：
# 现在，update_odometer() 在修改属性前检查指定的读数是否合理。如果新指定的里程（mileage ）大于或等
# 于原来的里程（self.odometer_reading ），就将里程表读数改为新指定的里程（见❶）；否则就发出警告
# ，指出不能将里程表往回拨（见❷）。

my_new_car.update_odometer(mileage=2)
my_new_car.read_odometer()


