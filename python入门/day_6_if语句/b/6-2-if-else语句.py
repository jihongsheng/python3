# -*- coding: UTF-8 -*-
"""经常需要在条件测试通过了时执行一个操作，并在没有通过时执行另一个操作；在这种情况
下，可使用Python提供的if-else 语句。if-else 语句块类似于简单的if 语句，但其中的else
语句让你能够指定条件测试未通过时要执行的操作。
下面的代码在一个人够投票的年龄时显示与前面相同的消息，同时在这个人不够投票的年龄时
也显示一条消息："""

age = 17
# 如果条件测试通过了，就执行第一个缩进的print 语句块；
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
# 如果测试结果为False ，就执行else 代码块。
# 这次age 小于18，条件测试未通过，因此执行else 代码块中的代码：
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
# 上述代码之所以可行，是因为只存在两种情形：要么够投票的年龄，要么不够。if-else
# 结构非常适合用于要让Python执行两种操作之一的情形。在这种简单的if-else 结构
# 中，总是会执行两个操作中的一个。
