# -*- coding: UTF-8 -*-
# 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。
# 在这种情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了
# 多少就接受多少。一个这样的示例是创建用户简介：你知道你将收到有关用户的信息
# ，但不确定会是什么样的信息。在下面的示例中，函数build_profile() 接受名和
# 姓，同时还接受任意数量的关键字实参：


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('1','2', 姓名='张三', 年龄=18)
print(user_profile)
for key, value in user_profile.items():
    print(key, value)
