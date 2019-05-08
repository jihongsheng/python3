# -*- coding: UTF-8 -*-
# 检查数值非常简单，例如，下面的代码检查一个人是否是18岁：
age = 18
print(age == 18)
print("-" * 80)

# 你还可以检查两个数字是否不等，例如，下面的代码在提供的答案不正确时打印一条消息：
answer = 17
if answer != 42:
    # answer （17 ）不是42 ，条件得到满足，因此缩进的代码块得以执行：
    print("That is not the correct answer. Please try again!")
print("-" * 80)

# 条件语句中可包含各种数学比较，如小于、小于等于、大于、大于等于：
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

