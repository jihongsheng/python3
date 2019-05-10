# -*- coding: UTF-8 -*-
# 有时候，需要让实参变成可选的，这样使用函数的人就只需要在必要时候才提供额外的信息。
# 可以使用默认值来让实参变成可选的。


# 例如，假设我们要扩展函数get_formatted_name() ，使其还处理中间名。为此，可将其修改
# 成类似于下面这样：
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = "%s %s %s" % (first_name, middle_name, last_name)
    return full_name.title()


# 只要同时提供名、中间名和姓，这个函数就能正确地运行。它根据这三部分创建一个字符串
# ，在适当的地方加上空格，并将结果转换为首字母大写格式：
musician = get_formatted_name('ji', 'hong', 'sheng')
print(musician)
"""
然而，并非所有的人都有中间名，但如果你调用这个函数时只提供了名和姓，它将不能正确
地运行。为让中间名变成可选的，可给实参middle_name 指定一个默认值——空字符串，并
在用户没有提供中间名时不使用这个实参。为让get_formatted_name() 在没有提供中间名
时依然可行，可给实参middle_name 指定一个默认值——空字符串，并将其移到形参列表的末尾：
"""


# 在这个示例中，姓名是根据三个可能提供的部分创建的。由于人都有名和姓，
# 因此在函数定义中首先列出了这两个形参。中间名是可选的，因此在函数定
# 义中最后列出该形参，并将其默认值设置为空字符串
def get_formatted_name(first_name, last_name,  middle_name=''):
    """返回整洁的姓名"""
    # 在函数体中，我们检查是否提供了中间名。Python将非空字符串解读为True ，
    # 因此如果函数调用中提供了中间名，if middle_name 将为True
    # 如果提供了中间，就将名、中间名和姓合并为姓名，然后将其修改为首字母大写格式，并
    # 返回到函数调用行。在函数调用行，将返回的值存储在变量musician 中；然后将这个变
    # 量的值打印出来
    if middle_name:
        full_name = "%s %s %s" % (first_name, middle_name, last_name)
    # 如果没有提供中间名，middle_name 将为空字符串，导致if 测试未通过，进而执行else
    # 代码块；只使用名和姓来生成姓名，并将设置好格式的姓名返回给函数调用行。在函数调
    # 用行，将返回的值存储在变量musician 中；然后将这个变量的值打印出来。
    else:
        full_name = "%s %s" % (first_name, last_name)
    return full_name.title()


musician = get_formatted_name(first_name='wang', last_name='fei')
print(musician)

# 调用这个函数时，如果只想指定名和姓，调用起来将非常简单。如果还要指定中间名，
# 就必须确保它是最后一个实参，这样Python才能正确地将位置实参关联到形参
musician = get_formatted_name(first_name='ji', middle_name='hong', last_name='sheng')
print(musician)
# 这个修改后的版本适用于只有名和姓的人，也适用于还有中间名的人
