# -*- coding: UTF-8 -*-


class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print("%s 蹲下了！" % self.name.title())

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print("%s 打滚了！" % self.name.title())


my_dog = Dog(name='小黑', age=6)
your_dog = Dog(name='小花', age=3)

print("我的小狗叫%s." % my_dog.name)
print("%s今年%s岁了" % (my_dog.name, str(my_dog.age)))
my_dog.sit()

print("\n他的小狗叫%s." % your_dog.name)
print("%s今年%s岁了" % (your_dog.name, str(your_dog.age)))
your_dog.roll_over()
# 在这个实例中，我们创建了两条小狗，它们分别名为Willie和Lucy。
# 每条小狗都是一个独立的实例，有自己的一组属性，能够执行相同的操作：

# 我的小狗叫小黑.
# 小黑今年6岁了
# 小黑 蹲下了！
#
# 他的小狗叫小花.
# 小花今年3岁了
# 小花 打滚了！

# 就算我们给第二条小狗指定同样的名字和年龄，Python依然会根据Dog 类创建另一个实例。你可按需求根据
# 一个类创建任意数量的实例，条件是将每个实例都存储在不同的变量中，或占用列表或字典的不同位置。
