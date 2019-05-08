# -*- coding: UTF-8 -*-
# 如果你感兴趣的主要是字典包含的值，可使用方法values() ，它返回一个值列表，而不包含任何键。例如，如果我
# 们想获得一个这样的列表，即其中只包含被调查者选择的各种语言，而不包含被调查者的名字，可以这样做：
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print("-" * 80)
# 这条for 语句提取字典中的每个值，并将它们依次存储到变量language 中。通过打印这些值，就获得了一个
# 列表，其中包含被调查者选择的各种语言：


# 这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不是问题，但如果被调查
# 者很多，最终的列表可能包含大量的重复项。为剔除重复项，可使用集合（set）。集合 类似于列表，但
# 每个元素都必须是独一无二的：
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):   # ❶
    print(language.title())
"""
通过对包含重复元素的列表调用set() ，可让Python找出列表中独一无二的元素，并使用这些元素来创建一个集合。在❶处，我们使用了set() 来提
取favorite_languages.values() 中不同的语言。
结果是一个不重复的列表，其中列出了被调查者提及的所有语言：
The following languages have been mentioned:
Python
C 
Ruby
"""
