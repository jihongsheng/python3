# -*- coding: UTF-8 -*-
# 你还可以导入模块中的特定函数，这种导入方法的语法如下：
# from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
# from module_name import function_0, function_1, function_2


# 对于当前的pizzas.py示例，如果想导入想要是用的函数，代码如下
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(20, 'mushrooms', 'green peppers', 'extra cheese')

# 若使用这种语法，调用函数时就无需使用句点。由于我们在import 语句中显式地导入了
# 函数make_pizza() ，因此调用它时只需指定其名称。
