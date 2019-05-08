# -*- coding: UTF-8 -*-
# 要判断两个值是否不等，可结合使用惊叹号和等号（!= ），其中的惊叹号表示不 ，在很多编程语言中都如此。
# 下面再使用一条if 语句来演示如何使用不等运算符。我们将把要求的比萨配料存储在一个变量中，再打印一条
# 消息，指出顾客要求的配料是否是意式小银鱼（anchovies）：

requested_topping = 'mushrooms'
# 处的代码行将requested_topping 的值与'anchovies' 进行比较，如果它们不相等，Python将返回True；
# 进而执行紧跟在if 语句后面的代码
# 如果这两个值相等，Python将返回False ，因此不执行紧跟在if语句后面的代码。
if requested_topping != 'anchovies':
    # 由于requested_topping的值不是'anchovies' ，因此执行print
    print("Hold the anchovies!")
