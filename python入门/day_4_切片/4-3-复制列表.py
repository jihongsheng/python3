# -*- coding: UTF-8 -*-
# 你经常需要根据既有列表创建全新的列表。下面来介绍复制列表的工作原理，以及复制列表可提供极大帮助的一种情形。
# 要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:] ）。这让Python创建一个始
# 于第一个元素，终止于最后一个元素的切片，即复制整个列表。
# 例如，假设有一个列表，其中包含你最喜欢的四种食品，而你还想创建另一个列表，在其中包含一位朋友喜欢的所有食品。
# 不过，你喜欢的食品，这位朋友都喜欢，因此你可以通过复制来创建这个列表：

# 我们首先创建了一个名为my_foods 的食品列表
my_foods = ['pizza', 'falafel', 'carrot cake']
# 然后创建了一个名为friend_foods 的新列表
friend_foods = my_foods[:]
# 我们在不指定任何索引的情况下从列表my_foods 中提取一个切片，从而创建了这个列表的副本，再将该副本存储到
# 变量friend_foods 中。打印每个列表后，我们发现它们包含的食品相同：
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print('-' * 80)


# 为核实我们确实有两个列表，下面在每个列表中都添加一种食品，并核实每个列表都记录了相应人员喜欢的食品：
my_foods = ['pizza', 'falafel', 'carrot cake']
# 我们首先将my_foods 的元素复制到新列表friend_foods 中
friend_foods = my_foods[:]
# 接下来，在每个列表中都添加一种食品：在列表my_foods 中添加'cannoli'
my_foods.append('cannoli')
# 而在friend_foods 中添加'ice cream'
friend_foods.append('ice cream')
# 最后，打印这两个列表，核实这两种食品包含在正确的列表中。
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print('-' * 80)

# 倘若我们只是简单地将my_foods 赋给friend_foods ，就不能得到两个列表。例如，下例演示了在不使用切片的
# 情况下复制列表的情况：
my_foods = ['pizza', 'falafel', 'carrot cake']
#这行不通
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

"""
这里将my_foods 赋给friend_foods ，而不是将my_foods 的副本存储到friend_foods 。这种语法实际上是让Python将新变量friend_foods 关联到包含
在my_foods 中的列表，因此这两个变量都指向同一个列表。鉴于此，当我们将'cannoli' 添加到my_foods 中时，它也将出现在friend_foods 中；同样，虽然'ice
cream' 好像只被加入到了friend_foods 中，但它也将出现在这两个列表中。"""