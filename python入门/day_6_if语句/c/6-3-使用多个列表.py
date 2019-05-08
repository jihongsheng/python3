# -*- coding: UTF-8 -*-

# 顾客的要求往往五花八门，在比萨配料方面尤其如此。如果顾客要在比萨中添加炸薯条，该怎么办呢？
# 可使用列表和if 语句来确定能否满足顾客的要求。来看看在制作比萨前如何拒绝怪异的配料要求。下面
# 的示例定义了两个列表，其中第一个列表包含比萨店供应的配料，而第二个列表包含顾客点的配料。这次对
# 于requested_toppings 中的每个元素，都检查它是否是比萨店供应的配料，再决定是否在比萨中添加它：
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']   # ❶
requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] # ❷
for requested_topping in requested_toppings:    # ❸
    if requested_topping in available_toppings: # ❹
        print("Adding " + requested_topping + ".")
    else:   # ❺
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

# 在❶处，我们定义了一个列表，其中包含比萨店供应的配料。请注意，如果比萨店供应的配料是固定的，也可使
# 用一个元组来存储它们。在❷处，我们又创建了一个列表，其中包含顾客点的配料，请注意那个不同寻常的配料
# ——'french fries' 。在❸处，我们遍历顾客点的配料列表。在这个循环中，对于顾客点的每种配料，我们都
# 检查它是否包含在供应的配料列表中（见❹）；如果答案是肯定的，就将其加入到比萨中，否则将运行else 代码
# 块（见❺）：打印一条消息，告诉顾客不供应这种配料。这些代码的输出整洁而详实：

