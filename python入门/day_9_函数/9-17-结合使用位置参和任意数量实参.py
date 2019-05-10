# -*- coding: UTF-8 -*-
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量的形参放在最后，python先
# 匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
# 例如，如果前面的函数还需要一个表示披萨尺寸的实参，必须要将形参放在形参*toppings前面：


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print('\n制造一个%s英寸比萨饼' % str(size))
    for x in toppings:
        print("\t-%s" % x.title())


make_pizza(16, 'pepperoni')
make_pizza(20, 'mushrooms', 'green peppers', 'extra cheese')

# 基于上述函数定义，python将受到的第一个值存储在形参size中，并将其他的所有值都存储在元
# 组toppings中，在函数调用中，首先指定表示比萨尺寸的实参，然后根据需要指定任意数量的材料。


