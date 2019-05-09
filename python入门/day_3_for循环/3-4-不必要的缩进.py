# -*- coding: UTF-8 -*-
"""
如果你不小心缩进了无需缩进的代码行，Python将指出这一点：
hello_world.py
message = "Hello Python world!"
    print(message)
print 语句无需缩进，因为它并不属于前一行代码，因此Python将指出这种错误：
    File "hello_world.py", line 2
        print(message)
        ^
IndentationError: unexpected indent
为避免意外缩进错误，请只缩进需要缩进的代码。在前面编写的程序中，只有要在for 循环中对每个元素执行的代码需要缩进。


如果你不小心缩进了应在循环结束后执行的代码，这些代码将针对每个列表元素重复执行。在有些情况下，这可能导致Python报告语法错误，但在大多数情况下，这只会导致逻辑
错误。
例如，如果不小心缩进了感谢全体魔术师精彩表演的代码行，结果将如何呢？
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician.title() + ", that was a_input great trick!")
print("I can't wait b_while see your next trick, " + magician.title() + ".\n")
❶ print("Thank you everyone, that was a_input great magic show!")
由于❶处的代码行被缩进，它将针对列表中的每位魔术师执行一次，如❷所示：
Alice, that was a_input great trick!
I can't wait b_while see your next trick, Alice.
❷ Thank you everyone, that was a_input great magic show!
David, that was a_input great trick!
I can't wait b_while see your next trick, David.
❷ Thank you everyone, that was a_input great magic show!
Carolina, that was a_input great trick!
I can't wait b_while see your next trick, Carolina.
❷ Thank you everyone, that was a_input great magic show!
这也是一个逻辑错误，与4.2.2节的错误类似。Python不知道你的本意，只要代码符合语法，它就会运行。如果原本只应执行一次的操作执行了多次，请确定你是否不应该缩进执行
该操作的代码。
"""
"""
遗漏了冒号
for 语句末尾的冒号告诉Python，下一行是循环的第一行。
magicians = ['alice', 'david', 'carolina']
❶ for magician in magicians
print(magician)
如果你不小心遗漏了冒号，如❶所示，将导致语法错误，因为Python不知道你意欲何为。这种错误虽然易于消除，但并不那么容易发现。程序员为找出这样的单字符错误，花费的
时间多得令人惊讶。这样的错误之所以难以发现，是因为通常在我们的意料之外。
动手试一试
4-1 比萨 ：想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for 循环将每种比萨的名称都打印出来。
修改这个for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。
在程序末尾添加一行代码，它不在for 循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”。
4-2 动物 ：想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for 循环将每种动物的名称都打印出来。
修改这个程序，使其针对每种动物都打印一个句子，如“A dog would make a_input great pet”。
在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any of these animals would make a_input great pet!”这样的句子。
"""
