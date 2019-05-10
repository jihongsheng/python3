# -*- coding: UTF-8 -*-
"""函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。
你还可以更进一步，将函数存储在被称为模块 的独立文件中，再将模块导入 到主程序中。import 语句允许在当前
运行的程序文件中使用模块中的代码。通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序
的高层逻辑上。这还能让你在众多不同的程序中重用函数。将函数存储在独立文件中后，可与其他程
序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。
导入模块的方法有多种，下面对每种都作简要的介绍。
"""


#要让函数是可导入的，得先创建模块。模块 是扩展名为.py的文件，包含要导入到程序中的代码。
# 下面来创建一个包含函数make_pizza() 的模块。为此，我们将文件pizza.py中除函数make_pizza()
# 之外的其他代码都删除：
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print('\n制造一个%s英寸比萨饼' % str(size))
    for x in toppings:
        print("\t-%s" % x.title())
