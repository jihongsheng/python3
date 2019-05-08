# -*- coding: UTF-8 -*-
# 在Python中检查是否相等时区分大小写，例如，两个大小写不同的值会被视为不相等：
car = 'Audi'
print(car == 'audi')
print("-" * 80)

# 如果大小写很重要，这种行为有其优点。但如果大小写无关紧要，而只想检查变量的值，可将变量的值转换为小写，再进行比较：
car = 'Audi'
# 无论值'Audi' 的大小写如何，上述测试都将返回True ，因为该测试不区分大小写。
# 函数lower() 不会修改存储在变量car 中的值，因此进行这样的比较时不会影响原来的变量：
print(car.lower() == 'audi')
print("-" * 80)


# 我们将首字母大写的字符串'Audi' 存储在变量car 中
car = 'Audi'
# 我们获取变量car 的值并将其转换为小写，再将结果与字符串'audi' 进行比较。这两个字符串相同，因此Python返回True
print(car.lower() == 'audi')
# 此处的输出可知，这个条件测试并没有影响存储在变量car 中的值。
print(car)