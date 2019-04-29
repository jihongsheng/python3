# -*- coding: UTF-8 -*-
# "Python方法sort() 让你能够较为轻松地对列表进行排序。假设你有一个汽车列表，
# 并要让其中的汽车按字母顺序排列。为简化这项任务，我们假设该列表中的所有值都是小写的。"
cars = ['bmw', 'audi', 'toyota', 'subaru']
# 方法sort();永久性地修改了列表元素的排列顺序。现在，汽车是按字母顺序排列的，再也无法恢复到原来的排列顺序：
cars.sort()
print(cars)
print("-" * 80)
# 你还可以按与字母顺序相反的顺序排列列表元素，为此，只需向sort() 方法传递参数reverse=True 。
# 下面的示例将汽车列表按与字母顺序相反的顺序排列：
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
print("-" * 80)
# 同样，对列表元素排列顺序的修改是永久性的：
