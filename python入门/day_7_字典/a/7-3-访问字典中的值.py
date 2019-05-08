# -*- coding: UTF-8 -*-
# 要获取与键相关联的值，可依次指定字典名和放在方括号内的键，如下所示：
alien_0 = {'color': 'green'}
print(alien_0['color'])

# 字典中可包含任意数量的键—值对。例如，下面是最初的字典alien_0 ，其中包含两个键—值对：
alien_0 = {'color': 'green', 'points': 5}

# 现在，你可以访问外星人alien_0 的颜色和点数。如果玩家射杀了这个外星人，你就可以使用下
# 面的代码来确定玩家应获得多少个点：
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']  # ❶
print("You just earned " + str(new_points) + " points!")    # ❷
# 上述代码首先定义了一个字典，然后从这个字典中获取与键'points' 相关联的值（见❶），并将这个
# 值存储在变量new_points 中。接下来，将这个整数转换为字符串，并打印一条消息，指出玩家获得了
# 多少个点（见❷）：
