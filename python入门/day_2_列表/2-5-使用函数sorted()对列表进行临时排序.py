# -*- coding: UTF-8 -*-
# 要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数sorted() 。函数sorted() 让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排
# 列顺序。
cars = ['bmw', 'audi', 'toyota', 'subaru']
# 我们首先按原始顺序打印列表
print("Here is the original list:")
print(cars)
# 再按字母顺序显示该列表
print("\nHere is the sorted list:")
print(sorted(cars))
# 以特定顺序显示列表后，我们进行核实，确认列表元素的排列顺序与以前相同
print("\nHere is the original list again:")
print(cars)
print("-" * 80)
# 注意，调用函数sorted() 后，列表元素的排列顺序并没有变
# 如果你要按与字母顺序相反的顺序显示列表，也可向函数sorted() 传递参数reverse=True 。
