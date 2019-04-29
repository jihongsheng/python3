# -*- coding: UTF-8 -*-
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组：

# 我们首先定义了一个元组，并将其存储的尺寸打印了出来
dimensions = (200, 50)       # ❶
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# 接下来，将一个新元组存储到变量dimensions 中
dimensions = (400, 100)         # ❷
# ；然后，打印新的尺寸
print("\nModified dimensions:")     # ❸
# 这次，Python不会报告任何错误，因为给元组变量赋值是合法的：
for dimension in dimensions:
    print(dimension)

