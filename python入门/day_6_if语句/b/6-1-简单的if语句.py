# -*- coding: UTF-8 -*-
# 理解条件测试后，就可以开始编写if 语句了。if 语句有很多种，选择使用哪种取决于要测试的条件数。
# 前面讨论条件测试时，列举了多个if 语句示例，下面更深入地讨论这个主题。
# 最简单的if 语句只有一个测试和一个操作：.


# 在第1行中，可包含任何条件测试，而在紧跟在测试后面的缩进代码块中，可执行任何操作。
# 如果条件测试的结果为True ，Python就会执行紧跟在if 语句后面的代码；否则Python将忽略这些代码。
# if conditional_test:
#     do something

# 假设有一个表示某人年龄的变量，而你想知道这个人是否够投票的年龄，可使用如下代码：
age = 19
# Python检查变量age 的值是否大于或等于18；答案是肯定的
if age >= 18:
    # 因此Python执行缩进的print语句
    print("You are old enough to vote!")
print("-*" * 40)

# 在if 语句中，缩进的作用与for 循环中相同。如果测试通过了，将执行if 语句后面所有缩进
# 的代码行，否则将忽略它们。
# 在紧跟在if 语句后面的代码块中，可根据需要包含任意数量的代码行。下面在一个人够投票的
# 年龄时再打印一行输出，问他是否登记了：
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")



# 如果age 的值小于18，这个程序将不会有任何输出。