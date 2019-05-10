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


# 根据Dog类创建实例后，就可以使用句点表示法来调用Dog类中定义的任何方法。下面来让小狗蹲下和打滚。
my_dog = Dog(name='小黑', age=6)
my_dog.sit()
my_dog.roll_over()
# 要调用方法，可指定实例的名称（这里是my_dog ）和要调用的方法，并用句点分隔它们。遇到代
# 码my_dog.sit() 时，Python在类Dog 中查找方法sit() 并运行其代码。Python以同样的方式解读
# 代码my_dog.roll_over() 。
# 小黑 蹲下了！
# 小黑 打滚了！
"""这种语法很有用。如果给属性和方法指定了合适的描述性名称，如name 、age 、sit() 和roll_over() ，
即便是从未见过的代码块，我们也能够轻松地推断出它是做什么"""

