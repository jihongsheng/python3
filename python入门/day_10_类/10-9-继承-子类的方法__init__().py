# -*- coding: UTF-8 -*-
# 编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用继承 。一个类继承
# 另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类 ，而新类称为子类 。子类继承了
# 其父类的所有属性和方法，同时还可以定义自己的属性和方法。


# 子类的方法__init__()
# 创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。为此，子类的方法__init__()
# 需要父类施以援手。
# 例如，下面来模拟电动汽车。电动汽车是一种特殊的汽车，因此我们可以在前面创建的Car 类的基础上创建
# 新类ElectricCar ，这样我们就只需为电动汽车特有的属性和行为编写代码。
# 下面来创建一个简单的ElectricCar 类版本，它具备Car 类的所有功能：
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


class ElectricCar(Car):     # ❷
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):      # ❸
        """初始化父类的属性"""
        super().__init__(make, model, year)        # ❹


# my_new_car = Car(make='奥迪', model='a4', year=2015)
# print(my_new_car.get_descriptive_name())
my_tesla = ElectricCar(make='特斯拉', model='model s', year=2016)      # ❺
print(my_tesla.get_descriptive_name())

# 首先是Car 类的代码（见❶）。创建子类时，父类必须包含在当前文件中，且位于子类前面。在❷处，我们定义
# 了子类ElectricCar 。定义子类时，必须在括号内指定父类的名称。方法__init__() 接受创建Car 实例所需的
# 信息（见❸）。
# ❹处的super() 是一个特殊函数，帮助Python将父类和子类关联起来。这行代码让Python调用ElectricCar 的父
# 类的方法__init__() ，让ElectricCar 实例包含父类的所有属性。父类也称为超类 （superclass），名称supe
# r因此而得名。
# 为测试继承是否能够正确地发挥作用，我们尝试创建一辆电动汽车，但提供的信息与创建普通汽车时相同。在
# ❺处，我们创建ElectricCar 类的一个实例，并将其存储在变量my_tesla 中。这行代码调用ElectricCar 类中
# 定义的方法__init__() ，后者让Python调用父类Car 中定义的方法__init__() 。我们提供了实参'tesla' 、'model
# s' 和2016 。
# 除方法__init__() 外，电动汽车没有其他特有的属性和方法。当前，我们只想确认电动汽车具备普通汽车的行为：
# 2016 特斯拉 Model S

# ElectricCar 实例的行为与Car 实例一样，现在可以开始定义电动汽车特有的属性和方法了。

