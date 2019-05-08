# -*- coding: UTF-8 -*-

# 修改字典中的值
# 要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。例如，
# 假设随着游戏的进行，需要将一个外星人从绿色改为黄色：
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
print("-" * 80)
# 我们首先定义了一个表示外星人alien_0 的字典，其中只包含这个外星人的颜色。接下来，我们
# 将与键'color' 相关联的值改为'yellow' 。输出表明，这个外星人确实从绿色变成了黄色：


# 来看一个更有趣的例子：对一个能够以不同速度移动的外星人的位置进行跟踪。为此，我们将存储
# 该外星人的当前速度，并据此确定该外星人将向右移动多远：
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
# 如果外星人的速度为'slow' ，它将向右移动一个单位；
if alien_0['speed'] == 'slow':  # ❶
    x_increment = 1
#  如果速度为'medium' ，将向右移动两个单位
elif alien_0['speed'] == 'medium':
    x_increment = 2
# 如果为'fast' ，将向右移动三个单位
else:
    # 这个外星人的速度一定很快
    x_increment = 3
    # 新位置等于老位置加上增量
# 确定移动量后，将其与x_position 的当前值相加;
alien_0['x_position'] = alien_0['x_position'] + x_increment     # ❷
# 再将结果关联到字典中的键x_position 。
print("New x-position: " + str(alien_0['x_position']))

# 我们首先定义了一个外星人，其中包含初始的x 坐标和y 坐标，还有速度'medium' 。出于简化考
# 虑，我们省略了颜色和点数，但即便包含这些键-值对，这个示例的工作原理也不会有任何变化。
# 我们还打印了x_position 的初始值，旨在让用户知道这个外星人向右移动了多远。

"""
在❶处，使用了一个if-elif-else 结构来确定外星人应向右移动多远，并将这个值存储在变量x_increment 中。如果外星人的速度为'slow' ，它将向右移动一个单位；
如果速度为'medium' ，将向右移动两个单位；如果为'fast' ，将向右移动三个单位。确定移动量后，将其与x_position 的当前值相加（见❷），再将结果关联到字典中
的键x_position 。"""
# 这种技术很棒：通过修改外星人字典中的值，可改变外星人的行为。例如，要将这个速度中等的外星
# 人变成速度很快的外星人，可添加如下代码行：
# alien_0['speed'] = fast
# 这样，再次运行这些代码时，其中的if-elif-else 结构将把一个更大的值赋给变量x_increment 。
