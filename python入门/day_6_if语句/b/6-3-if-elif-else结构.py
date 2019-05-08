# -*- coding: UTF-8 -*-
"""
经常需要检查超过两个的情形，为此可使用Python提供的if-elif-else 结构。Python只执行if-elif-else
结构中的一个代码块，它依次检查每个条件测试，直到遇到通过了的条件测试。测试通过后，Python将执
行紧跟在它后面的代码，并跳过余下的测试。
在现实世界中，很多情况下需要考虑的情形都超过两个。例如，来看一个根据年龄段收费的游乐场：
4岁以下免费；
4~18岁收费5美元；
18岁（含）以上收费10美元。
如果只使用一条if 语句，如何确定门票价格呢？下面的代码确定一个人所属的年龄段，并打印一条包含
门票价格的消息：
"""
age = 12
# if 测试检查一个人是否不满4岁，如果是这样，Python就打印一条合适的消息，并跳过余下的测试。
if age < 4:     # ❶
    print("Your admission cost is $0.")
# elif 代码行其实是另一个if 测试，它仅在前面的测试未通过时才会运行。在这里，我们知道这个人不
# 小于4岁，因为第一个测试未通过。如果这个人未满18岁，Python将打印相应的消息，并跳过else 代码块
elif age < 18:
    print("Your admission cost is $5.")
# 如果if 测试和elif 测试都未通过，Python将运行else 代码块中的代码。
else:
    print("Your admission cost is $10.")
# 在这个示例中，❶处测试的结果为False ，因此不执行其代码块。然而，第二个测试的结果为True
# （12小于18），因此将执行其代码块。输出为一个句子，向用户指出了门票价格：
# 只要年龄超过17岁，前两个测试就都不能通过。在这种情况下，将执行else 代码块，指出门票价
# 格为10美元。
print("*" * 80)

# 为让代码更简洁，可不在if-elif-else 代码块中打印门票价格，而只在其中设置门票价格，并在它
# 后面添加一条简单的print 语句：
age = 12
if age < 4:
    price = 0       # ❶
elif age < 18:
    price = 5       # ❷
else:
    price = 10      # ❸
print("Your admission cost is $" + str(price) + ".")    # ❹
print("Your admission cost is $%s. " % price)    # ❹
"""
❶处、❷处和❸处的代码行像前一个示例那样，根据人的年龄设置变量price 的值。在if-elif-else 结构
中设置price 的值后，一条未缩进的print 语句❹会根据这个变量的值打印一条消息，指出门票的价格。
这些代码的输出与前一个示例相同，但if-elif-else 结构的作用更小，它只确定门票价格，而不是在
确定门票价格的同时打印一条消息。除效率更高外，这些修订后的代码还更容易修改：要调整输出消息
的内容，只需修改一条而不是三条print 语句。"""