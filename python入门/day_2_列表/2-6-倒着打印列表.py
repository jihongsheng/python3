# -*- coding: UTF-8 -*-
# 要反转列表元素的排列顺序，可使用方法reverse() 。假设汽车列表是按购买时间排列的，可轻松地按相反的顺序排列其中的汽车：
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
# 注意，reverse() 不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序：
# 方法reverse() 永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用reverse() 即可。
cars.reverse()
print(cars)
