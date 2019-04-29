# -*- coding: UTF-8 -*-
# 列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网站的用户列表或
# 游戏中的角色列表至关重要。然而，有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。
# Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组 。

# 定义元组

# 元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
# 例如，如果有一个大小不应改变的矩形，可将其长度和宽度存储在一个元组中，从而确保它们是不能修改的：

# 我们首先定义了元组dimensions
dimensions = (200, 50)
# 为此我们使用了圆括号而不是方括号。接下来，我们分别打印该元组的各个元素，使用的语法与访问列表元素时使用的语法相同
print(dimensions[0])
print(dimensions[1])

# 下面来尝试修改元组dimensions 中的一个元素，看看结果如何：
"""
dimensions = (200, 50)
试图修改第一个元素的值，导致Python返回类型错误消息。由于试图修改元组的操作是被禁止的，因此Python指出不能给
元组的元素赋值：
dimensions[0] = 250
Traceback (most recent call last):
  File "E:/python3-github/python入门/day_5_元组/5-1-定义元组.py", line 19, in <module>
    dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment

代码试图修改矩形的尺寸时，Python报告错误，这很好，因为这正是我们希望的。
"""