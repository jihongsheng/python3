# -*- coding: UTF-8 -*-
def greet_user(username):       # username 形参
    print("Hello,%s!" % username)


greet_user('Jhs')
# greet_user(username='Jhs')   Jhs是实参;将Jhs 传输给了函数greet_user(),这个值被存储在username中
"""
上面定义函数greet_user()时，要求给变量username指定一个值，调用这个函数并提供这种信息（人名）
时，它将打印相应的问候语。
在函数greet_user()的定义中，变量username是一个形参 - - - 函数完成其工作所需的一项信息。
在代码greet_user('Jhs')中，将实参'Jhs'传输给了函数greet_user(),这个值被存储在形参username中。

大家有时候会形参、实参不分，因此如果你看到有人将函数定义中的变量称为实参或将函数调用中的变量
称为形参，不要大惊小怪。

"""


