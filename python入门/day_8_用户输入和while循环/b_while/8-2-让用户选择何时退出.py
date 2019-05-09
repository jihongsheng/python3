# -*- coding: UTF-8 -*-
# 可使用while 循环让程序在用户愿意时不断地运行，如下面的程序parrot.py所示。
# 我们在其中定义了一个退出值，只要用户输入的不是这个值，程序就接着运行：

# while message != 'quit':
#     message = input(number)
#     print(message)

while True:
    message = input("输入一个数字，我会告诉你它是偶数还是奇数：")
    if message == "quit":
        break
    if int(message) % 2 == 0:
        print("数字 %s 是偶数" % str(message))
    elif int(message) % 2 == 1:
        print("数字 %s 是奇数" % str(message))


