# -*- coding: UTF-8 -*-
"""
在程序中，额外的空白可能令人迷惑。对程序员来说，'python' 和'python ' 看起来几乎没什么两样，
但对程序来说，它们却是两个不同的字符串。Python能够发现'python ' 中额外的空白，并认为它是有
意义的——除非你告诉它不是这样的。
"""
favorite_language = 'python '
print(favorite_language)
# favorite_language.rstrip() 方法去掉空白
# 要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中：
favorite_language = favorite_language.rstrip()
print(favorite_language)

# 我们首先创建了一个开头和末尾都有空白的字符串
favorite_language = ' python '
print(favorite_language)
# 删除末尾 .rstrip() 的空格
print(favorite_language.rstrip())
# 删除开头 .lstrip() 的空格
print(favorite_language.lstrip())
# 删除两端 .strip() 的空格
print(favorite_language.strip())



