# -*- coding: UTF-8 -*-
# 要创建数字列表，可使用函数list() 将range() 的结果直接转换为列表。如果将range() 作为list() 的参数，
# 输出将为一个数字列表。在前一节的示例中，我们打印了一系列数字。要将这些数字转换为一个列表，可使用list() ：
numbers = list(range(1,6))
print(numbers)
print("-"*80)
# 使用函数range() 时，还可指定步长。例如，下面的代码打印1~10内的偶数：
# 在这个示例中，函数range() 从2开始数，然后不断地加2，直到达到或超过终值（11），因此输出如下：
even_numbers = list(range(2,11,2))
print(even_numbers)
print("-"*80)
even_numbers = list(range(1,11,2))
print(even_numbers)
print("-"*80)

# 使用函数range() 几乎能够创建任何需要的数字集，例如，如何创建一个列表，其中包含前10个整数（即1~10）的平方呢？
# 在Python中，两个星号（** ）表示乘方运算。下面的代码演示了如何将前10个整数的平方加入到一个列表中：
# 首先，我们创建了一个空列表
squares = []
# 接下来，使用函数range() 让Python遍历1~10的值
for value in range(1,11):
    # 在循环中，计算当前值的平方，并将结果存储到变量square中
    square = value**2
    # 然后，将新计算得到的平方值附加到列表squares 末尾
    squares.append(square)
    # print(squares)
# 最后，循环结束后，打印列表squares
print(squares)
print("-"*80)
# 为让这些代码更简洁，可不使用临时变量square ，而直接将每个计算得到的值附加到列表末尾：
squares = []
for value in range(1,11):
    # 在循环中，计算每个值的平方，并立即将结果附加到列表squares的末尾。
    squares.append(value**2)
print(squares)
# 创建更复杂的列表时，可使用上述两种方法中的任何一种。有时候，使用临时变量会让代码更易读；
# 而在其他情况下，这样做只会让代码无谓地变长。你首先应该考虑的是，编
# 写清晰易懂且能完成所需功能的代码；等到审核代码时，再考虑采用更高效的方法。
