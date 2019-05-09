# -*- coding: UTF-8 -*-

prompt = "输入一个数字，我会告诉你它是偶数还是奇数："

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)



prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


