# -*- coding: UTF-8 -*-


# 下面来编写一个表示汽车的类，它存储了有关汽车的信息，还有一个汇总这些信息的方法：
class Car():
    """一次模拟汽车的简单尝试"""
    # 定义方法__init__()。与前面的Dog类中一样，这个方法的第一个形参为self:我们还在这个方法中包含三个
    # 形参：make、model和year.方法__init__()接受这些形参的值，并将它们存储在根据这个类创建的实例的属性
    # 中。创建新的Car实例时，我们需要指定其造商、型号和生产年份。
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    # 我们定义了一个名为get_descriptive_name() 的方法，它使用属性year 、make 和model 创建一个对汽车进
    # 行描述的字符串，让我们无需分别打印每个属性的值。为在这个方法中访问属性的值，我们使用了self.make
    # 、self.model 和self.year 。
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = "%s %s %s" % (str(self.year), self.make, self.model)
        return long_name.title()


# 我们根据Car 类创建了一个实例，并将其存储到变量my_new_car中。接下来，我们调用方法get_descriptive_name()
# ，指出我们拥有的是一辆什么样的汽车：
my_new_car = Car(make='奥迪', model='a4', year=2016)
print(my_new_car.get_descriptive_name())
# 为让这个类更有趣，下面给它添加一个随时间变化的属性，它存储汽车的总里程。



