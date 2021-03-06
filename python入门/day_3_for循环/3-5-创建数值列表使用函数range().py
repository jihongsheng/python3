# -*- coding: UTF-8 -*-
"""
需要存储一组数字的原因有很多，例如，在游戏中，需要跟踪每个角色的位置，还可能需要跟踪玩家的几个最高得分。在数据可视化中，
处理的几乎都是由数字（如温度、距离、人口数量、经度和纬度等）组成的集合。
列表非常适合用于存储数字集合，而Python提供了很多工具，可帮助你高效地处理数字列表。明白如何有效地使用这些工具后，即便列
表包含数百万个元素，你编写的代码也能运行得很好。
"""
# 使用函数range()
# Python函数range() 让你能够轻松地生成一系列的数字。例如，可以像下面这样使用函数range() 来打印一系列的数字：
for value in range(1,5):
    print(value)
# 上述代码好像应该打印数字1~5，但实际上它不会打印数字5：
# 在这个示例中，range() 只是打印数字1~4，这是你在编程语言中经常看到的差一行为的结果。函数range() 让Python从你指定的第一个值开始数，并在到达你指定的第二个值
# 后停止，因此输出不包含第二个值（这里为5）。
# 要打印数字1~5，需要使用range(1,6) ：
print("-" * 80)
for value in range(1,6):
    print(value)
# 这样，输出将从1开始，到5结束：