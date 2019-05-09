# -*- coding: UTF-8 -*-
"""
到目前为止，我们每次都只处理了一项用户信息：获取用户的输入，再将输入打印出来或作出应答；循环再
次运行时，我们获悉另一个输入值并作出响应。然而，要记录大量的用户和信息，需要在while 循环中使
用列表和字典。
for 循环是一种遍历列表的有效方式，但在for 循环中不应修改列表，否则将导致Python难以跟踪其中的元
素。要在遍历列表的同时对其进行修改，可使用while 循环。通过将while 循环同列表和字典结合起来使
用，可收集、存储并组织大量输入，供以后查看和显示。
"""
# 假设有一个列表，其中包含新注册但还未验证的网站用户；验证这些用户后，如何将他们移到另一个已验
# 证用户列表中呢？一种办法是使用一个while 循环，在验证用户的同时将其从未验证用户列表中提取
# 出来，再将其加入到另一个已验证用户列表中。代码可能类似于下面这样：

# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print(unconfirmed_users)
print(confirmed_users)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 练习
number = [1, 2, 3, 4]
num_old = []

while number:
    num_old_won = number.pop()
    num_old.append(num_old_won)
print(number)
print(num_old)
for name in num_old:
    print(name)

