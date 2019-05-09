# -*- coding: UTF-8 -*-
"""到目前为止，对于处理的每个列表都做了一个简单的假设，即假设它们都至少包含一个元素。我们马上就要让
用户来提供存储在列表中的信息，因此不能再假设循环运行时列表不是空的。有鉴于此，在运行for 循环前确定列
表是否为空很重要。
下面在制作比萨前检查顾客点的配料列表是否为空。如果列表是空的，就向顾客确认他是否要点普通比萨；如果列
表不为空，就像前面的示例那样制作比萨：
"""

requested_toppings = [] # ❶
if requested_toppings:  # ❷
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:   # ❸
    print("Are you sure you want a_input plain pizza?")


# 在这里，我们首先创建了一个空列表，其中不包含任何配料（见❶）。在❷处我们进行了简单检查，而不是直接执
# 行for 循环。在if 语句中将列表名用在条件表达式中时，Python将在列表至少包含一个元素时返回True ，并在
# 列表为空时返回False 。如果requested_toppings 不为空，就运行与前一个示例相同的for 循环；否则，就打印
# 一条消息，询问顾客是否确实要点不加任何配料的普通比萨（见❸）。在这里，这个列表为空，因此输出如下——
# 询问顾客是否确实要点普通比萨：

