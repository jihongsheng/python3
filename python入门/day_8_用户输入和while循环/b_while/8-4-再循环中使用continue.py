# -*- coding: UTF-8 -*-
# 要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue 语句，
# 它不像break 语句那样不再执行余下的代码并退出整个循环。例如，来看一个从1数
# 到10，但只打印其中偶数的循环：
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

