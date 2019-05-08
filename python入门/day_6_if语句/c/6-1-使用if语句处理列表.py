# -*- coding: UTF-8 -*-
# 通过结合使用if 语句和列表，可完成一些有趣的任务：对列表中特定的值做特殊处理；高效地管理不断
# 变化的情形，如餐馆是否还有特定的食材；证明代码在各种情形下都将按预期那样运行。

# 检查特殊元素
"""
本章开头通过一个简单示例演示了如何处理特殊值'bmw' ——它需要采用不同的格式进行打印。既然你对
条件测试和if 语句有了大致的认识，下面来进一步研究如何检查列表中的特殊值，并对其做合适的处理。
继续使用前面的比萨店示例。这家比萨店在制作比萨时，每添加一种配料都打印一条消息。通过创建一个
列表，在其中包含顾客点的配料，并使用一个循环来指出添加到比萨中的配料，可以以极高的效率编写这
样的代码：
"""
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
# 输出很简单，因为上述代码不过是一个简单的for循环
print("-" * 80)
# 然而，如果比萨店的青椒用完了，该如何处理呢？为妥善地处理这种情况，可在for 循环中包含一条if 语句：
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':    # ❶
        print("Sorry, we are out of green peppers right now.")
    else:       # ❷
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

# 这里在比萨中添加每种配料前都进行检查。❶处的代码检查顾客点的是否是青椒，如果是，就显示一
# 条消息，指出不能点青椒的原因。❷处的else 代码块确保其他配料都将添加到比萨中。
# 输出表明，妥善地处理了顾客点的每种配料：










