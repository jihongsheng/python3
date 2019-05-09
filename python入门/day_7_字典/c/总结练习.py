# -*- coding: UTF-8 -*-

name_0 = {'姓名': '张三', '年龄': 18, '籍贯': '陕西'}
name_1 = {'姓名': '李四', '年龄': 28, '籍贯': '北京'}
name_2 = {'姓名': '王五', '年龄': 38, '籍贯': '上海'}

people = [name_0, name_1, name_2]

for x in people:
    print(x)
    for k, value in x.items():
        print(k, value)




