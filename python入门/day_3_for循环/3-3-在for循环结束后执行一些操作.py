# -*- coding: UTF-8 -*-
"""
for 循环结束后再怎么做呢？通常，你需要提供总结性输出或接着执行程序必须完成的其他任务。
在for 循环后面，没有缩进的代码都只执行一次，而不会重复执行。下面来打印一条向全体魔术师致谢的消息，
感谢他们的精彩表演。想要在打印给各位魔术师的消息后面打印
一条给全体魔术师的致谢消息，需要将相应的代码放在for 循环后面，且不缩进：
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")
# 你在前面看到了，开头两条print 语句针对列表中每位魔术师重复执行。然而，由于第三条print 语句没有缩进，因此只执行一次：
# 使用for 循环处理数据是一种对数据集执行整体操作的不错的方式。例如，你可能使用for 循环来初始化游戏—
# —遍历角色列表，将每个角色都显示到屏幕上；再在循环后面添加一个不缩进的代码块，在屏幕上绘制所有角色后显示一个Play Now按钮。
