# -*- coding: UTF-8 -*-
# 在for 循环中，可对每个元素执行任何操作。下面来扩展前面的示例，对于每位魔术师，都打印一条消息，指出他的表演太精彩了。
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # 相比于前一个示例，唯一的不同是对于每位魔术师，都打印了一条以其名字为抬头的消息
    # 这个循环第一次迭代时，变量magician的值为'alice' ，因此Python打印的第一条消息的抬头为
    # 'Alice' 。第二次迭代时，消息的抬头为'David' ，而第三次迭代时，抬头为'Carolina' 。
    print(magician.title() + ", that was a great trick!")
print("-"*80)

"""
在for 循环中，想包含多少行代码都可以。在代码行for magician in magicians 后面，每个缩进的代码行都是循环的一部分，且将针对列表中的每个值都执行一次。因
此，可对列表中的每个值执行任意次数的操作。
下面再添加一行代码，告诉每位魔术师，我们期待他的下一次表演：
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
"""
由于两条print 语句都缩进了，因此它们都将针对列表中的每位魔术师执行一次。第二条print 语句中的换行符"\n" 
在每次迭代结束后都插入一个空行，从而整洁地将针对各位魔术师的消息编组：
在for 循环中，想包含多少行代码都可以。实际上，你会发现使用for 循环对每个元素执行众多不同的操作很有用。
"""