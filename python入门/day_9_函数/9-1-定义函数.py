# -*- coding: UTF-8 -*-


# 下面是一个打印问候的简单函数，名为greet_user():
def greet_user():   # ❶
    """显示简单的问候语句"""     # ❷
    print("Hello!")     # ❸


greet_user()        # ❹

# 这个示例演示了最简单的函数结构。❶处的代码行使用关键字def 来告诉Python你要定义一个函数
# 。这是函数定义 ，向Python指出了函数名，还可能在括号内指出函数为完成其
# 任务需要什么样的信息。在这里，函数名为greet_user() ，它不需要任何信息就能完成其工作，
# 因此括号是空的（即便如此，括号也必不可少）。最后，定义以冒号结尾。
# 紧跟在def greet_user(): 后面的所有缩进行构成了函数体。❷处的文本是被称为文档字符串
# （docstring）的注释，描述了函数是做什么的。文档字符串用三引号括起，Python使用它们
# 来生成有关程序中函数的文档。
# 代码行print("Hello!") （见❸）是函数体内的唯一一行代码，greet_user() 只做一项工作：
# 打印Hello! 。
# 要使用这个函数，可调用它。函数调用 让Python执行函数的代码。要调用 函数，可依次指
# 定函数名以及用括号括起的必要信息，如❹处所示。由于这个函数不需要任何信息，因
# 此调用它时只需输入greet_user() 即可。和预期的一样，它打印Hello! ：

