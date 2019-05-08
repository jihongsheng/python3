# -*- coding: UTF-8 -*-

# 如果要遍历列表的部分元素，可在for 循环中使用切片。在下面的示例中，我们遍历前三名队员，并打印他们的名字：
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first c players on my team:")
# 此处的代码没有遍历整个队员列表，而只遍历前三名队员：
for player in players[:3]:
    print(player.title())
# 在很多情况下，切片都很有用。例如，编写游戏时，你可以在玩家退出游戏时将其最终得分加入到一个列表中。
# 然后，为获取该玩家的三个最高得分，你可以将该列表按降序排列，再创建一个只包含前三个得分的切片。处理数据时，
# 可使用切片来进行批量处理；编写Web应用程序时，可使用切片来分页显示信息，并在每页显示数量合适的信息。