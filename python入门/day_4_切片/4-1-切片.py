# -*- coding: UTF-8 -*-

"""
要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range() 一样，Python在到达你指定的第二个
索引前面的元素后停止。要输出列表中的前三个元素，需要指定索引0~3，这将输出分别为0 、1 和2 的元素。
"""
# 下面的示例处理的是一个运动队成员列表：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 打印该列表的一个切片，其中只包含三名队员。输出也是一个列表，其中包含前三名队员：
print(players[0:3])
print("-" * 80)
# 可以生成列表的任何子集，例如，如果你要提取列表的第2~4个元素，可将起始索引指定为1 ，并将终止索引指定为4 ：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 这一次，切片始于’marita' ，终于'florence' ：
print(players[1:4])
print("-" * 80)
# 如果你没有指定第一个索引，Python将自动从列表开头开始：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
print("-" * 80)
# 要让切片终止于列表末尾，也可使用类似的语法。例如，如果要提取从第3个元素到列表末尾的所有元素，可将起始索
# 引指定为2 ，并省略终止索引：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

# 无论列表多长，这种语法都能够让你输出从特定位置到列表末尾的所有元素。本书前面说过，负数索引返回离列表
# 末尾相应距离的元素，因此你可以输出列表末尾的任何切片。例如，如果你要输出名单上的最后三名队员，可
# 使用切片players[-3:] ：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
# 上述代码打印最后三名队员的名字，即便队员名单的长度发生变化，也依然如此。

