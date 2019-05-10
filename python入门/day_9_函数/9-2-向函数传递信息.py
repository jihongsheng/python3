# -*- coding: UTF-8 -*-


# 只需稍作修改，就可以让函数greet_user() 不仅向用户显示Hello! ，还将用户的名字用作抬头。
# 为此，可在函数定义def greet_user() 的括号内添加username 。通过在这里添加username ，就
# 可让函数接受你给username 指定的任何值。现在，这个函数要求你调用它时给username 指定一
# 个值。调用greet_user() 时，可将一个名字传递给它，如下所示：
def greet_user(username):
    print("Hello,%s!" % username)


# 代码greet_user(username="Wang") 调用函数greet_user() ，并向它提供执行print 语句所需的信息。
greet_user(username="Wang")
# 同样，greet_user('Ji') 调用函数greet_user() 并向它传递'Ji' ，打印Hello, Ji! 。
greet_user("Ji")


# 你可以根据需要调用函数greet_user() 任意次，调用时无论传入什么样的名字，都会生成相应的输出。

