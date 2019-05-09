# -*- coding: UTF-8 -*-

# 使用函数input() 时，Python将用户输入解读为字符串。请看下面让用户输入其年龄的
# 解释器会话：
age = input("请输入你的年龄： ")
# 用户输入的数字返回的是字符串
print(age)

# 如果要比较，首先要将字符串转换为数字类型
age = int(age)
print(age >= 18)


# 如何在实际程序中使用函数int() 呢？请看下面的程序，它判断一个人是否满足坐
# 过山车的身高要求：
height = int(input("请输入你的身高： "))
if height >= 36:
    print("可以乘坐过山车")
else:
    print("不能称作过山车")