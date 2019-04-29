# -*- coding: UTF-8 -*-
# 有几个专门用于处理数字列表的Python函数。例如，你可以轻松地找出数字列表的最大值、最小值和总和：
digits = list(range(0, 10))
print(digits)
# 最小值   min()
print(min(digits))
# 最大值   max()
print(max(digits))
# 总和    sum()
print(sum(digits))

digits = list(range(1, 101, 2))
print(digits)
print(sum(digits))
digits = list(range(2, 101, 2))
print(digits)
print(sum(digits))
# 出于版面考虑，本节使用的数字列表都很短，但这里介绍的知识也适用于包含数百万个数字的列表。
