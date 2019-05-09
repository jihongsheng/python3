# -*- coding: UTF-8 -*-
# 假设你有一个宠物列表，其中包含多个值为'cat' 的元素。要删除所有这些元素
# ，可不断运行一个while 循环，直到列表中不再包含值'cat' ，如下所示：
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
# 我们首先创建了一个列表，其中包含多个值为'cat' 的元素。打印这个列表后，Python进
# 入while 循环，因为它发现'cat' 在列表中至少出现了一次。进入这个循环后，Python
# 删除第一个'cat' 并返回到while 代码行，然后发现'cat' 还包含在列表中，因此再次
# 进入循环。它不断删除'cat' ，直到这个值不再包含在列表中，然后退出循环并再次打
# 印列表：
number = [1, 2, 3, 3, 2, 5, 6, 3, 2]
while 1 in number:
    number.remove(1)
print(number)

