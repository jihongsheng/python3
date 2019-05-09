# -*- coding: UTF-8 -*-
name_number = {}

item = True

while item:
    name = input('你叫什么名字？')
    number = input('你喜欢哪个数字？')

    name_number[name] = number

    input_ord = input("是否介绍自己同事 (yes/ no)")
    if input_ord == "no":
        item = False
print(name_number)
for name, number in name_number.items():
    print("%s 喜欢数字 %s" % (name, number))


