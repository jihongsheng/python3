# -*- coding: UTF-8 -*-
import pizza
# 接下来，我们在pizza.py所在的目录中创建另一个名为making_pizzas.py的文件，这个文件导入刚创建的模块，
# 再调用make_pizza() 两次：making_pizzas.
# Python读取这个文件时，代码行import pizza 让Python打开文件pizza.py，并将其中的所有函数都复制到这个
# 程序中。你看不到复制的代码，因为这个程序运行时，Python在幕后复制这些代码。你只需知道，在making_pi
# zzas.py中，可以使用pizza.py中定义的所有函数。
# 要调用被导入的模块中的函数，可指定导入的模块的名称pizza 和函数名make_pizza() ，并用句点分隔它们
# （见❶）。这些代码的输出与没有导入模块的原始程序相同：
pizza.make_pizza('pepperoni')   # ❶
pizza.make_pizza('mushrooms', 'green peppers', 'extra cheese')
# make_pizza(16, 'pepperoni')
# make_pizza(20, 'mushrooms', 'green peppers', 'extra cheese')
# 这就是一种导入方法：只需编写一条import 语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。
# 如果你使用这种import 语句导入了名为module_name.py的整个模块，就可使用下面的语法来使用其中任何一个函数：