# -*- coding: UTF-8 -*-
# 鉴于可混合使用位置实参，关键字实参和默认值，通常有多种等效的函数调用方式，请看下面
# describe_pets()的定义，其中给一个形参提供了默认值：


def describe_pet(pet_name, animal_type='小狗'):
    """显示宠物信息"""
    print("\n我有一个%s." % animal_type)
    print("%s的名字叫%s." % (animal_type, pet_name))
# 基于这种定义，在任何情况下都必须给pet_name提供实参：指定该实参可以使用位置方式，也
# 可以使用关键字方式。如果要描述动物不是小狗，还必须在函数中给animal_type提供实参：
# 同样，指定该实参是可以使用的位置方式，也可以使用关键字方式


# 一条名为小黑黑的小狗
describe_pet('小黑黑')
describe_pet(pet_name='小黑黑')

# 一直名为小飞飞的小鸟
describe_pet('小飞飞', '小鸟')
describe_pet(pet_name='小飞飞', animal_type='小鸟')
describe_pet(animal_type='小鸟', pet_name='小飞飞')
# 这些函数调用的输出与前面的示例相同。
# 注意 　使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行。
# 使用对你来说最容易理解的调用方式即可。
