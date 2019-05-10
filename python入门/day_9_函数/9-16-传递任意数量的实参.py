# -*- coding: UTF-8 -*-
# 有时候，你预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任意数量的实参。
# 例如，来看一个制作比萨的函数，它需要接受很多配料，但你无法预先确定顾客要多少种配料。
# 下面的函数只有一个形参*toppings ，但不管调用语句提供了多少实参，这个形参都将它们统统收入囊中：


# 形参名 *toppings 中的星号让python创建一个名为toppings的空元组，并将收到的所有值封装到这个元组中
# 函数体print语句通过生成输出来证明python能够处理使用一个值调用函数的情形，也能处理使用三个值来调用
# 函数的情形，它以类似的方式处理不同的调用，注意，python将实参封装到一个元组中，几遍函数只收到一个
# 值也如此
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    # 不管收到的是一个值还是三个值，这个函数都能妥善地处理：
    print("\n制作披萨的材料有：")
    for x in toppings:
        print("\t%s" % x.title())


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# 不管函数收到的实参是多少个，这种语法都管用。

