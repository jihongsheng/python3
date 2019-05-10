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


# 这里使用上面编写的Dog类我们让python创建一个名字为‘小黑’年龄为6的小狗，遇到这行代码时，python使用实参
# 小黑和6调用dog类中方法__init__()创建一个表示特定小狗的示例，并使用我们提供的值来设置属性name和age.方法
# __init__()并未显示地包含return语句，单python自动返回一个表示这条小狗的实例，我们将我们将这个实例存储在
# 变量my_dog 中。在这里，命名约定很有用：我们通常可以认为首字母大写的名称（如Dog ）指的是类，而小写的名
# 称（如my_dog ）指的是根据类创建的实例。
my_dog = Dog(name='小黑', age=6)

# 要访问实例的属性，可使用句点表示法。我们编写了如下代码来访问my_dog 的属性name 的值：
print("我的小狗叫%s." % my_dog.name)
# 我们使用同样的方法来获取属性age 的值
print("%s今年%s岁了" % (my_dog.name, str(my_dog.age)))
