# -*- coding: UTF-8 -*-
# 在不需要使用字典中的值时，方法keys() 很有用。下面来遍历字典favorite_languages ，并将每个被调
# 查者的名字都打印出来：
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys():  # ❶
    print(name.title())
# ❶处的代码行让Python提取字典favorite_languages 中的所有键，并依次将它们存储到变量name 中。
# 输出列出了每个被调查者的名字：
# 遍历字典时，会默认遍历所有的键，因此，如果将上述代码中的for name in favorite_languages.keys():
# 替换为for name in favorite_languages: ，输出将不变。
print("-" * 80)


"""
如果显式地使用方法keys() 可让代码更容易理解，你可以选择这样做，但如果你愿意，也可省略它。
在这种循环中，可使用当前键来访问与之相关联的值。下面来打印两条消息，指出两位朋友喜欢的语言。
我们像前面一样遍历字典中的名字，但在名字为指定朋友的名字时，打印一条消息，指出其喜欢的语言：
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
# 我们创建了一个列表，其中包含我们要通过打印消息，指出其喜欢的语言的朋友
friends = ['phil', 'sarah']     # ❶
for name in favorite_languages.keys():
    print(name.title())
    # 在循环中，我们打印每个人的名字，并检查当前的名字是否在列表friends中
    if name in friends:     # ❷
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            # 如果在列表中，就打印一句特殊的问候语，其中包含这位朋友喜欢的语言。
            # 为访问喜欢的语言，我们使用了字典名，并将变量name 的当前值作为键
            favorite_languages[name].title() + "!")     # ❸
        # 每个人的名字都会被打印，但只对朋友打印特殊消息：
# 你还可以使用keys() 确定某个人是否接受了调查。下面的代码确定Erin是否接受了调查：

print("-" * 80)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in favorite_languages.keys():     # ❶
    print("Erin, please take our poll!")
# 方法keys() 并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键，因此❶处的
# 代码行只是核实'erin' 是否包含在这个列表中。由于她并不包含在这个列表中，因此打印一条消息，
# 邀请她参加调查：



