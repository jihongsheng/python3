# -*- coding: UTF-8 -*-
# 字典总是明确地记录键和值之间的关联关系，但获取字典的元素时，获取顺序是不可预测的。这不是问题，
# 因为通常你想要的只是获取与键相关联的正确的值。要以特定的顺序返回元素，一种办法是在for 循环中
# 对返回的键进行排序。为此，可使用函数sorted() 来获得按特定顺序排列的键列表的副本：
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 这条for 语句类似于其他for 语句，但对方法dictionary.keys() 的结果调用了函数sorted() 。这让Python
# 列出字典中的所有键，并在遍历前对这个列表进行排序。输出表明，按顺序显示了所有被调查者的名字：
