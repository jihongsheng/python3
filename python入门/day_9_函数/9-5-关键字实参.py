# -*- coding: UTF-8 -*-
# 关键字实参 是传递给函数的名称—值对。你直接在实参中将名称和值关联起来了，
# 因此向函数传递实参时不会混淆（不会得到名为Hamster的harry这样的结果）。关键字实参让
# 你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\n我有一个%s." % animal_type)
    print("%s的名字叫%s." % (animal_type, pet_name))


# 关键字实参的顺序无关紧要，因为Python知道各个值该存储到哪个形参中。
# 下面两个函数调用是等效的：
describe_pet(animal_type="小狗", pet_name="小黑黑")

describe_pet(pet_name="小黑黑", animal_type="小狗")

# 注意 　使用关键字实参时，务必准确地指定函数定义中的形参名。
