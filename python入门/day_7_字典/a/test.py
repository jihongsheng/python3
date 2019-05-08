# -*- coding: UTF-8 -*-

'''
# 首先定义一个字典，
one = {'name': 'Jhs',
       'age': 18}
# 然后从这个字典中获取与键'age'相关的值，并将这个值存储在my_age中
my_age = one['age']
# 将这个整数转换为字符串，并打印一条消息，显示年龄
print('My name is %s！' % str(my_age))
print('My name is ' + str(my_age) + '!')
print('*' * 80)

print(one)
# 我们在这个字典中新增了一个键—值对，其中的键为'email' ，而值为'6909283@qq.com'
one['email'] = "6909283@qq.com"
# 我们重复这样的操作，但使用的键为'y_position' 。
one['Telephone'] = 13127623512
# 打印修改后的字典时，将看到这两个新增的键—值对：
print(one)
"""
这个字典的最终版本包含四个键—值对，其中原来的两个指定年龄和姓名，而新增的两个指定电话和email。
注意，键—值对的排列顺序与添加顺序不同。Python不关心键—值对的添加顺序，而只关心键和值之间的关
联关系。
"""
'''

'''
# 空字典中添加键--值
one = {}
one['name'] = 'Jhs'
one['age'] = 18
print(one)
'''

# 修改字典的值
# 要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。
# 例如，我们将名字替换

# 首先我们定义一个one字典，其中姓名为
# one = {'name': 'Jhs'}
# print('My name is %s.' % one['name'] )
#
# one['name'] = 'Lbl'
# print('My name is now %s.' % one['name'])


"""
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x-position: %s" % str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3



alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: %s' % str(alien_0['x_position']))
"""

"""
# 删除键--值对
# 对于字典中不再需要的信息，可使用del 语句将相应的键—值对彻底删除。使用del 语句时，必须指定
# 字典名和要删除的键。例如，下面的代码从字典alien_0 中删除键'points' 及其值：
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['color']
print(alien_0)
# 删除的键—值对永远消失了。
"""

# you_love = {
#     '张三': 'python',
#     '李四': 'Java',
#     '王五': 'PhP',
#     '赵六': 'Python',
# }
# print("张三最喜欢的语言是 %s." % you_love['张三'].title())

# oen = {'first_name': '宝玲', 'last_name': '吕', 'age': 25, 'city': '陕西'}
# print(oen)
# print(oen['first_name'])
# print(oen['last_name'])
# print(oen['age'])
# print(oen['city'])
#
# tow = {'张三': 1, '李四': 2, '王五': 3, '赵六': 4, '宋七': 5}
# print("张三喜欢的数字是 %s." % (tow['张三']))
# print("李四喜欢的数字是 %s." % (tow['李四']))
# print("王五喜欢的数字是 %s." % (tow['王五']))
# print("赵六喜欢的数字是 %s." % (tow['赵六']))
# print("宋七喜欢的数字是 %s." % (tow['宋七']))


tow = {'张三': '唱歌', '李四': '跳舞', '王五': '打游戏'}
print("*"*80)
for key, value in tow.items():
    print("姓名: %s" % key)
    print("爱好: %s" % value)
print("*"*80)

tow = {'age': 18, 'name': 'yellow', 'like': 'family'}
for k, v in tow.items():
    print("%s---%s" % (k, v))
print("*"*80)
like_name = {
    'song': 'python',
    'wang': 'c#',
    'lv': 'java',
    'ji': 'php'
}
# favorite 语言，懒鬼吃。。。I im favorite people is Lv Baoling  # My favorite person is Lv Baoling
for name, language in like_name.items():
    print("%s's favorite language is %s." % (name.title(), language.title()))


favorite = {'name': 'lv baoling', 'age': 25}
# for k, v in favorite.items():
print('My favorite people is %s, she is age %s.' % (favorite["name"].title(), favorite["age"]))


# 遍历字典中的所有键
# 在不需要使用字典中的值时，方法keys() 很有用
# print("*"*80)
# like_name = {
#     'song': 'python',
#     'wang': 'c#',
#     'lv': 'java',
#     'ji': 'php'
# }
#
# for name in like_name.keys():
#     print(name)

# print("*"*80)
# like_name = {
#     'song': 'python',
#     'wang': 'c#',
#     'lv': 'java',
#     'ji': 'php'
# }
# name_1 = ['ji', 'wang']
# for name in like_name.keys():
#     print(name.title())
#
#     if name in name_1:
#         print('Hi %s, Isee your favorite language is %s!'
#               % (name.title(), like_name[name].title()))

# print("*"*80)
# like_name = {
#     'song': 'python',
#     'wang': 'c#',
#     'lv': 'java',
#     'ji': 'php'
# }
# # 你还可以使用keys() 确定某个人是否接受了调查。下面的代码确定Erin是否接受了调查：
# if 'erin' not in like_name.keys():
#     print('Erin, please take our poll!')

# 按照顺序遍历字典中的值
# print("*"*80)
# like_name = {
#     'song': 'python',
#     'wang': 'c#',
#     'lv': 'java',
#     'ji': 'php'
# }
# 按照顺序遍历字典中的值;sorted按升序返回所有项的新列表。
# for name in sorted(like_name.keys()):
#     print('%s,thank you for taking the poll.' % name.title())
# for name in like_name.values():
#     print('喜欢的语言是%s' % name.title())
# for name in sorted(like_name.values()):
#     print('喜欢的语言是%s' % name.title())

print("*"*80)
like_name = {
    'song': 'python',
    'wang': 'php',
    'lv': 'java',
    'ji': 'php'
}
# 使用set（）去掉重复
for name in set(like_name.values()):
    print(name.title())
