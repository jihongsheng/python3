# -*- coding: UTF-8 -*-

"""
有时候，执行操作前必须检查列表是否包含特定的值。例如，结束用户的注册过程前，可能需要检查他提供的用户
名是否已包含在用户名列表中。在地图程序中，可能需要检查用户提交的位置是否包含在已知位置列表中。
要判断特定的值是否已包含在列表中，可使用关键字in 。来看你可能为比萨店编写的一些代码；这些代码首先创建
一个列表，其中包含用户点的比萨配料，然后检查特定的配料是否包含在该列表中。
"""
requested_toppings = ['mushrooms', 'onions', 'pineapple']
# 关键字in 让Python检查列表requested_toppings 是否包含'mushrooms' 和'pepperoni' 。这种技术很有用，
# 它让你能够在创建一个列表后，轻松地检查其中是否包含特定的值。
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)