# -*- coding: UTF-8 -*-
# ❶ 修改元素
# 我们首先定义一个摩托车列表，其中的第一个元素为'honda'
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# 接下来，我们将第一个元素的值改为'ducati'
motorcycles[0] = 'ducati'
# 输出表明，第一个元素的值确实变了，但
# 其他列表元素的值没变：
print(motorcycles)

# ❷ 在列表中添加元素
print("-" * 80)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

print("-" * 80)
# 方法append() 让动态地创建列表易如反掌，例如，你可以先创建一个空列表，再使用
# 一系列的append() 语句添加元素。下面来创建一个空列表，再在其中添加元
# 素'honda' 、'yamaha' 和'suzuki' ：
motorcycles = []
motorcycles.append('张三')
motorcycles.append('李四')
motorcycles.append('王五')
print(motorcycles)

print("-" * 80)

# ❸ 从列表中删除元素
print("1. 使用del 语句删除元素")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
# 代码使用del删除了列表motorcycles中的第一个元素---'honda'
print(motorcycles)

print("-" * 80)
# 使用del可删除任何位置的列表元素，条件是是知道其索引。下例演示了如何删除前述
# 列表中的第二个元素——'yamaha' ：
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]  # 索引1 对应的元素2
print(motorcycles)

print("-" * 80)
print("2. 使用方法pop() 删除元素")
# 有时候，你要将元素从列表中删除，并接着使用它的值。
# 例如，你可能需要获取刚被射杀的外星人的 x 和 y 坐标，以便在相应的位置显示爆炸效果；
# 在Web应用程序中，你可能要将用户从活跃成员列表中删除，并将其加入到非活跃成员列表中。
# 方法pop() 可删除列表末尾的元素，并让你能够接着使用它。
# 术语弹出 （pop）源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
motorcycles = ['honda', 'yamaha', 'suzuki']
# 我们首先定义并打印了列表motorcycles
print(motorcycles)
# 接下来，我们从这个列表中弹出一个值，并将其存储到变量popped_motorcycle 中
popped_motorcycle = motorcycles.pop()
# 然后我们打印这个列表，以核实从其中删除了一个值
print(motorcycles)
# 最后，我们打印弹出的值，以证明我们依然能够访问被删除的值
print(popped_motorcycle)

print("-" * 80)
# 方法pop() 是怎么起作用的呢？假设列表中的摩托车是按购买时间存储的，
# 就可使用方法pop() 打印一条消息，指出最后购买的是哪款摩托车：
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
# 输出是一个简单的句子，指出了最新购买的是哪款摩托车：
print("The last motorcycle I owned was a_input " + last_owned.title() + ".")

print("-" * 80)
print("3. 弹出列表中任何位置处的元素")
# 实际上，你可以使用pop() 来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。
motorcycles = ['honda', 'yamaha', 'suzuki']
# 首先，我们弹出了列表中的第一款摩托车
first_owned = motorcycles.pop(0)
# 然后打印了一条有关这辆摩托车的消息
print('The first motorcycle I owned was a_input ' + first_owned.title() + '.')

"""
别忘了，每当你使用pop() 时，被弹出的元素就不再在列表中了。
如果你不确定该使用del 语句还是pop() 方法，下面是一个简单的判断标准：如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del 语句；如果你要在删除元
素后还能继续使用它，就使用方法pop() 。
"""
print("-" * 80)
print("4. 根据值删除元素")
# 有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，
# 可使用方法remove() 。
# 例如，假设我们要从列表motorcycles 中删除值'ducati' 。
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# 让Python确定'ducati' 出现在列表的什么地方，并将该元素删除：
motorcycles.remove('ducati')
print(motorcycles)
print("-" * 80)
# 使用remove() 从列表中删除元素时，也可接着使用它的值。下面删除值'ducati' ，
# 并打印一条消息，指出要将其从列表中删除的原因：
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# 值'ducati' 存储在变量too_expensive 中
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
# 我们使用这个变量来告诉Python将哪个值从列表中删除
print(motorcycles)
# 值'ducati' 已经从列表中删除，但它还存储在变量too_expensive 中
print("\nA " + too_expensive.title() + " is too expensive for me.")
# 注意 　方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，
# 就需要使用循环来判断是否删除了所有这样的值
