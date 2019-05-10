# -*- coding: UTF-8 -*-
"""
如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名
 ——函数的另一个名称，类似于外号。要给函数指定这种特殊外号，需要在导入它时这样做。
下面给函数make_pizza() 指定了别名mp() 。这是在import 语句中使用make_pizza as mp 实现的，关键字as
 将函数重命名为你提供的别名：
"""
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 上面的import 语句将函数make_pizza() 重命名为mp() ；在这个程序中，每当需要调用make_pizza() 时，
# 都可简写成mp() ，而Python将运行make_pizza() 中的代码，这可避免与这个程序可能包含的函
# 数make_pizza() 混淆。

# from module_name import function_name as fn
