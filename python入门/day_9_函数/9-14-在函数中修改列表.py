# -*- coding: UTF-8 -*-
# 将列表传递给函数后，函数就可以对其进行修改。在函数中对这个列表所做的任何修改都是永
# 久性的，这让你能够高效的处理大量的数据。


# 来看一家为用户提交的设计制作3D打印机模型公司，需要打印的设计存储在一个列表中，打印
# 后移到另一个列表中，下面是在不使用函数的情况下模拟这个过程的代码：
# 首先创建一个列表，其中包含一些要打印的设计
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# # 模拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移到列表completed_models中
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     #模拟根据设计制作3D打印模型的过程
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
# # 显示打印好的所有模型
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

"""这个程序首先创建一个需要打印的设计列表，还创建一个名为completed_models 的空列表，
每个设计打印都将移到这个列表中。只要列表unprinted_designs 中还有设计，while 循环就
模拟打印设计的过程：从该列表末尾删除一个设计，将其存储到变量current_design 中，并
显示一条消息，指出正在打印当前的设计，再将该设计加入到列表completed_models 中。
循环结束后，显示已打印的所有设计：
number = [1, 2, 3, 4]
num = []
while number:
    num_old = number.pop()
    num.append(num_old)
print(number)
for n in num:
    print(n)
"""


# 为重组这些代码，我们可以编写两个函数，每个都做一件具体的工作。大部分代码都与原来相同
# 只是效率更高。第一个函数将负责打印设计的工作，而第二个将概述打印了哪些设计：

# 我们定义了函数print_models() ，它包含两个形参：一个需要打印的设计列表和一个打印好的
# 模型列表。给定这两个列表，这个函数模拟打印每个设计的过程：将设计逐个地从未打印的设计列
# 表中取出，并加入到打印好的模型列表中
def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，知道没有来打印的设计为止
    打印每个设计后，都将其移动到列表completed_models中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: %s" % current_design)
        completed_models.append(current_design)


# 我们定义了函数show_completed_models() ，它包含一个形参：打印好的模型列表。给定
# 这个列表，函数show_completed_models() 显示打印出来的每个模型的名称。
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


"""
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
我们创建了一个未打印的设计列表，还创建了一个空列表，用于存储打印好的模型。接下来，由于我们已经定
义了两个函数，因此只需调用它们并传入正确的实参即可。我们调用print_models() 并向它传递两个列表；像预期
的一样，print_models() 模拟打印设计的过程。接下来，我们调用show_completed_models() ，并将打印好的模型
列表传递给它，让其能够指出打印了哪些模型。描述性的函数名让别人阅读这些代码时也能明白，虽然其中没有任
何注释。
相比于没有使用函数的版本，这个程序更容易扩展和维护。如果以后需要打印其他设计，只需再次调用print_models() 
即可。如果我们发现需要对打印代码进行修改，只需修改这些代码一次，就能影响所有调用该函数的地方；
与必须分别修改程序的多个地方相比，这种修改的效率更高。
这个程序还演示了这样一种理念，即每个函数都应只负责一项具体的工作。第一个函数打印每个设计，而第二个显示打
印好的模型；这优于使用一个函数来完成两项工作。编写函数时，如果你发现它执行的任务太多，请尝试将这些代
码划分到两个函数中。别忘了，总是可以在一个函数中调用另一个函数，这有助于将复杂的任务划分成一系列的步骤。
"""