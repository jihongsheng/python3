# -*- coding: UTF-8 -*-
# 可使用while循环提示用户输入任意数量的信息。下面来创建一个调查程序，其中的循环每次执行
# 时都提示输入被调查者的名字和回答。我们将收集的数据存储在一个字典中，以便将回答同被调
# 查者关联起来：
responses = {}

# 设置一个标准，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输被调查者的名字和回答
    name = input("\n你叫什么名字？")
    response = input("有一天你想爬哪座山？")

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("是否要让其他人响应？（yes/ no）")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- 投票结果 ---")
for name, response in responses.items():
    print("%s 想想去爬 %s." % (name, response))



