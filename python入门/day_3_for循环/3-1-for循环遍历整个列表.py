# -*- coding: UTF-8 -*-
# 你经常需要遍历列表的所有元素，对每个元素执行相同的操作。例如，在游戏中，可能需要将每个界面元素平移
# 相同的距离；对于包含数字的列表，可能需要对每个元素执行相同的统计运算；在网站中，可能需要显示文章列
# 表中的每个标题。需要对列表中的每个元素都执行相同的操作时，可使用Python中的for 循环。
# 假设我们有一个魔术师名单，需要将其中每个魔术师的名字都打印出来。为此，我们可以分别获取名单中的每个名字，
# 但这种做法会导致多个问题。例如，如果名单很长，将包含大量重复的代码。另外，每当名单的长度发生变化时，
# 都必须修改代码。通过使用for 循环，可让Python去处理这些问题。

# 首先，我们像第3章那样定义了一个列表
magicians = ['alice', 'david', 'carolina']
# 接下来，我们定义了一个for 循环（这行代码让Python从列表magicians 中取出一个名字，并将其存储在变量magician 中
for magician in magicians:
    # 最后，我们让Python打印前面存储到变量magician中的名字
    print(magician)

"""
magicians = ['alice', 'david', 'carolina']
循环这种概念很重要，因为它是让计算机自动完成重复工作的常见方式之一。例如，在前面的magicians.py中使用的简单循环中，Python将首先读取其中的第一行代码：
for magician in magicians:
这行代码让Python获取列表magicians 中的第一个值（'alice' ），并将其存储到变量magician 中。接下来，Python读取下一行代码：
print(magician)
它让Python打印magician 的值——依然是'alice' 。鉴于该列表还包含其他值，Python返回到循环的第一行：
for magician in magicians:
Python获取列表中的下一个名字——'david' ，并将其存储到变量magician 中，再执行下面这行代码：
print(magician)

Python再次打印变量magician 的值——当前为'david' 。接下来，Python再次执行整个循环，对列表中的最后一个值——'carolina' 
进行处理。至此，列表中没有其他的值了，因此Python接着执行程序的下一行代码。在这个示例中，for 循环后面没有其他的代码，
因此程序就此结束。
刚开始使用循环时请牢记，对列表中的每个元素，都将执行循环指定的步骤，而不管列表包含多少个元素。如果列表包含一百万个元素，
Python就重复执行指定的步骤一百万次，且通常速度非常快。
另外，编写for 循环时，对于用于存储列表中每个值的临时变量，可指定任何名称。然而，选择描述单个列表元素的有意义的名称大
有帮助。例如，对于小猫列表、小狗列表和一般性列表，像下面这样编写for 循环的第一行代码是不错的选择：
"""
"""
另外，编写for 循环时，对于用于存储列表中每个值的临时变量，可指定任何名称。然而，选择描述单个列表元素的有意义的名称大
有帮助。例如，对于小猫列表、小狗列表和一般性列表，像下面这样编写for 循环的第一行代码是不错的选择：
for cat in cats:
for dog in dogs:
for item in list_of_items:
这些命名约定有助于你明白for 循环中将对每个元素执行的操作。使用单数和复数式名称，可帮助你判断代码段处理的是单个列表元素还是整个列表。
"""