# -*- coding: UTF-8 -*-
# 函数并非总是直接显示输出，相反，他可以处理一些数据，并返回一个或一组值，函数返回的值
# 被称为返回值。在函数中，可以使用return语句将值返回到调用函数的代码行。返回值让你能够
# 将程序的大部分繁琐工作转移到函数中去完成，从而简化主程序。
# 下面来看一个函数，他接受名和性返回整洁的姓名


# 函数get_formatted_name() 的定义通过形参接受名和姓
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    # full_name = first_name.title() + ' ' + last_name.title()
    # 它将姓和名合而为一，在它们之间加上一个空格，并将结果存储在变量full_name 中
    full_name = "%s %s" % (first_name, last_name)
    # 然后，将full_name 的值转换为首字母大写格式，并将结果返回到函数调用行
    return full_name.title()


# 调用返回值的函数时，需要提供一个变量，用于存储返回的值。在这里，
# 将返回值存储在了变量musician 中。输出为整洁的姓名：
musician = get_formatted_name('ji', 'hongsheng')
print(musician)

# 我们原本只需编写下面的代码就可输出整洁的姓名，相比于此，前面做的工作好像太多了
print("Ji Hongsheng")
# 但在需要分别存储大量名和姓的大型程序中，像get_formatted_name() 这样的函数非常
# 有用。你分别存储名和姓，每当需要显示姓名时都调用这个函数。
