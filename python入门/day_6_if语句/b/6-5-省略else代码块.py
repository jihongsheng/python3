# -*- coding: UTF-8 -*-
# Python并不要求if-elif 结构后面必须有else 代码块。在有些情况下，else 代码块很有用；而
# 在其他一些情况下，使用一条elif 语句来处理特定的情形更清晰：
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:     # ❶
    price = 5
print("Your admission cost is $" + str(price) + ".")
# ❶处的elif 代码块在顾客的年龄超过65（含）时，将价格设置为5美元，这比使用else 代码块更清晰些。
# 经过这样的修改后，每个代码块都仅在通过了相应的测试时才会执行。
# else 是一条包罗万象的语句，只要不满足任何if 或elif 中的条件测试，其中的代码就会执行，这可能
# 会引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个elif 代码块来代替else 代码
# 块。这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。

