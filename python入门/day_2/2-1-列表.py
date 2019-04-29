# -*- coding: UTF-8 -*-

# 在Python中，用方括号（[] ）来表示列表，并用逗号来分隔其中的元素。
# 下面是一个简单的列表示例，这个列表包含几种自行车：
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# 索引是0开始而不是1，下面去出第0个索引；
print(bicycles[0].title())
# 我们取出索引第1个和第3个自行车： 返回结果是第二个和第4个元素
print(bicycles[1].title())
print(bicycles[3].title())

# Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1 ，可让Python返回最后一个列表元素：
print(bicycles[-1].title())

