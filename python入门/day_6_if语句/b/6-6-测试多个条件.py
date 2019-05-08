# -*- coding: UTF-8 -*-
# if-elif-else 结构功能强大，但仅适合用于只有一个条件满足的情况：遇到通过了的测试后，Python
# 就跳过余下的测试。这种行为很好，效率很高，让你能够测试一个特定的条件。
# 然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含elif 和else 代码块的
# 简单if 语句。在可能有多个条件为True ，且你需要在每个条件为True时都采取相应措施时，适合使用
# 这种方法。
# 下面再来看前面的比萨店示例。如果顾客点了两种配料，就需要确保在其比萨中包含这些配料：
requested_toppings = ['mushrooms', 'extra cheese']  # ❶
if 'mushrooms' in requested_toppings:   # ❷
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:   #❸
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:    # ❹
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
# 我们首先创建了一个列表，其中包含顾客点的配料（见❶）。❷处的if 语句检查顾客是否点了配料
# 蘑菇（'mushrooms' ），如果点了，就打印一条确认消息。❸处检查配料辣香肠（'pepperoni' ）的
# 代码也是一个简单的if 语句，而不是elif 或else 语句；因此不管前一个测试是否通过，都将进行
# 这个测试。❹处的代码检查顾客是否要求多加芝士（'extra cheese' ）；不管前两个测试的结果如何
# ，都会执行这些代码。每当这个程序运行时，都会进行这三个独立的测试。
# 在这个示例中，会检查每个条件，因此将在比萨中添加蘑菇并多加芝士：
print("*" * 80)

# 如果像下面这样转而使用if-elif-else 结构，代码将不能正确地运行，因为有一个测试通过后，就会跳过余下的测试：
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# 第一个测试检查列表中是否包含'mushrooms' ，它通过了，因此将在比萨中添加蘑菇。然而，Python将跳过if-elif-else 结构中余下的测试，不再检查列表中是否包
# 含'extra cheese' 和'pepperoni' 。其结果是，将添加顾客点的第一种配料，但不会添加其他的配料：