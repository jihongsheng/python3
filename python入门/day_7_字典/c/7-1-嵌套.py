# -*- coding: UTF-8 -*-

# 嵌套
# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套 。你可以在列表中嵌
# 套字典、在字典中嵌套列表甚至在字典中嵌套字典。正如下面的示例将演示的，嵌套是一项强大的功能。

# 字典列表
# 字典alien_0 包含一个外星人的各种信息，但无法存储第二个外星人的信息，更别说屏幕上全部外星人的信息了。
# 如何管理成群结队的外星人呢？一种办法是创建一个外星人列表，其中每个外星人都是一个字典，包含有关该外
# 星人的各种信息。例如，下面的代码创建一个包含三个外星人的列表：

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)
# print("-" * 80)

# number = []
# for x in range(30):
#     number.append(x)
# print(number)


'''
# 首先创建了一个空列表aliens，用于存储接下来将创建的所有外星人
aliens = []
# range() 返回一系列数字，其唯一的用途是告诉Python我们要重复这个循环多少次
for alien_number in range(30):
    # 每次执行这个循环时，都创建一个外星人
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    # 并将其附加到列表aliens末尾
    aliens.append(new_alien)
# print(aliens)
# 使用一个切片来打印前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
# 打印列表的长度，以证明确实创建了30个外星人：
print("Total number of aliens: %s" % str(len(aliens)))
'''

aliens = []
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0: 5]:
    print(alien)
print("...")

