# -*- coding: UTF-8 -*-
# 你还可以给模块指定别名。通过给模块指定简短的别名（如给模块pizza 指定别名p ），让你能够更
# 轻松地调用模块中的函数。相比于pizza.make_pizza()，p.make_pizza() 更为简洁：
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 上述import 语句给模块pizza 指定了别名p ，但该模块中所有函数的名称都没变。调用函数make_pizza() 时，
# 可编写代码p.make_pizza() 而不是pizza.make_pizza() ，这样不仅能使代码更简洁，还可以让你不再关注模
# 块名，而专注于描述性的函数名。这些函数名明确地指出了函数的功能，对理解代码而言，它们比模块名更重要。
# 给模块指定别名的通用语法如下：

# import module_name as mn
