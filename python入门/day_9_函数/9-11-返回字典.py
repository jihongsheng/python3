# -*- coding: UTF-8 -*-


# 函数可返回任何类型的值，包括列表和字典等比较复杂的数据结构。
# 例如，下面函数接受姓名的组成部分，并返回一个表示人的字典：
# 函数build_person() 接受名和姓，并将这些值封装到字典中
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    # 存储first_name 的值时，使用的键为'first' ，而存储last_name 的值时，使用的键
    # 为'last'
    person = {'first': first_name.title(), 'last': last_name.title()}
    return person


# 最后，返回表示人的整个字典，打印这个返回的值，此时原来的两项文本信息存储在一个字典中：
musician = build_person('ji', 'hongsheng')
print(musician)
# 这个函数接受简单的文本信息，将其放在一个更合适的数据结构中，让你不仅能打印这些信息，
# 还能以其他方式处理它们。当前，字符串'ji' 和'hongsheng' 被标记为名和姓。你可以轻松
# 地扩展这个函数，使其接受可选值，如中间名、年龄、职业或你要存储的其他任何信息。例如，下面的修改让你还能存储年龄：


def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person(first_name='ji', last_name='hongsheng', age='26')
print(musician)
# 在函数定义中，我们新增了一个可选形参age ，并将其默认值设置为空字符串。如果函数
# 调用中包含这个形参的值，这个值将存储到字典中。在任何情况下，这个函数都会存储
# 人的姓名，但可对其进行修改，使其也存储有关人的其他信息。
