# -*- coding: UTF-8 -*-
# 一个Python字典可能只包含几个键—值对，也可能包含数百万个键—值对。鉴于字典可能包含大量的数据，
# Python支持对字典遍历。字典可用于以各种方式存储信息，因此有多种遍历字典的方式：可遍历字典的所有
# 键—值对、键或值。

# 探索各种遍历方法前，先来看一个新字典，它用于存储有关网站用户的信息。下面的字典存储一名用户的
# 用户名、名和姓：
# 利用本章前面介绍过的知识，可访问user_0 的任何一项信息，但如果要获悉该用户字典中的所有信息，该
# 怎么办呢？可以使用一个for 循环来遍历这个字典：

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
# 要编写用于遍历字典的for 循环，可声明两个变量，用于存储键—值对中的键和值。对于这两个变量，
# 可使用任何名称；下面的代码使用了简单的变量名，这完全可行：
# for k, v in user_0.items():   # for 语句的第二部分包含字典名和方法items();（见❶）它返回一个键
# —值对列表。接下来，for 循环依次将每个键—值对存储到指定的两个变量中我
# 们使用这两个变量来打印每个键（见❷）及其相关联的值（见❸）。第一条print 语句中的"\n" 确保在输出每个键—值对前都插入一个空行：
for key, value in user_0.items():   # ❶
    print("\nKey: " + key)  # ❷
    print("Value: " + value)    # ❸
# 注意，即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序
# ，而只跟踪键和值之间的关联关系。
print("-" * 80)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():   # ❶
    print(name.title() + "'s favorite language is " +   # ❷
language.title() + ".")
"""
处的代码让Python遍历字典中的每个键—值对，并将键存储在变量name 中，而将值存储在变量language 中。这些描述性名称能够让人非常轻松地明白print 语句（见❷）
是做什么的。
仅使用几行代码，我们就将全部调查结果显示出来了：
Jen's favorite language is Python.
Sarah's favorite language is C.
Phil's favorite language is Python.
Edward's favorite language is Ruby.
即便字典存储的是上千乃至上百万人的调查结果，这种循环也管用。
"""





