# -*- coding: UTF-8 -*-
# 每当你使用函数input() 时，都应指定清晰而易于明白的提示，准确地指出
# 你希望用户提供什么样的信息——指出用户该输入任何信息的提示都行，如下所示：
name = input("please enter your name: ")
print("Hello, %s" % name)

# 有时候，提示可能超过一行，例如，你可能需要指出获取特定输入的原因。在
# 这种情况下，可将提示存储在一个变量中，再将该变量传递给函数input() 。
# 这样，即便提示超过一行，input() 语句也非常清晰。
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
# 这个示例演示了一种创建多行字符串的方式。第1行将消息的前半部分存储在变
# 量prompt 中；在第2行中，运算符+= 在存储在prompt 中的字符串末尾附加一个字符串。
# 最终的提示横跨两行，并在问号后面包含一个空格，这也是出于清晰考虑：

