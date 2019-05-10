# -*- coding: UTF-8 -*-
# 等你开始使用函数时候，如果遇到实参不匹配错误，不要大惊小怪，你提供的实参多于或少于
# 函数完成工作所需要的信息时，将出现实参不匹配错误。
# 例如，如果调用函数describe_pet()时没有指定任何实参，结果将如何？


def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\n我有一个%s." % animal_type)
    print("%s的名字叫%s." % (animal_type, pet_name))


describe_pet()

"""ython发现该函数调用缺少必要的信息，而traceback指出了这一点：
Traceback (most recent call last):      
  File "9-8-避免实参错误.py", line 13, in <module>        ❶
    describe_pet()      ❷
TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'     # ❸ 

"""
# 在❶处，traceback指出了问题出在什么地方，让我们能够回过头去找出函数调用中的错误。在❷处，指出
# 了导致问题的函数调用。在❸处，traceback指出该函数调用少两个实参，并指出了相应形参的名称。
# 如果这个函数存储在一个独立的文件中，我们也许无需打开这个文件并查看函数的代码，就能重新正确地编写函
# 数调用。
# Python读取函数的代码，并指出我们需要为哪些形参提供实参，这提供了极大的帮助。这也是应该给变量和函数
# 指定描述性名称的另一个原因；如果你这样做了，那么无论对于你，还是可能使用你编写的代码的其他任何人来
# 说，Python提供的错误消息都将更有帮助。如果提供的实参太多，将出现类似的traceback，帮助你确保函数调用
# 和函数定义匹配。