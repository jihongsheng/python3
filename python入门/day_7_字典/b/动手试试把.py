# -*- coding: UTF-8 -*-

# rivers = {
#     'china': 'yellow river',
#     'japan': 'pearl river',
#     'canada': 'yangtze river',
# }
# for key, value in rivers.items():
#     print('The %s runs through %s.' % (value.title(), key.title()))
# for name in rivers.keys():
#     print('国家是%s' % name.title())
# for name in rivers.values():
#     print('河流是%s' % name.title())


like_name = {
    '张三': 'python',
    '李四': 'java',
    '王五': 'c#',
    '赵六': 'shell',
    '宋七': 'php',
}
name_1 = ['张三', '王五', '宋七', '服了']

# for name in like_name.keys():
#     if name in name_1:
#         print('谢谢您的配合')
#     else:
#         print('请接受调查')
for name in name_1:
    if name not in like_name.keys():
        print('%s请接受调查！' % name)
    else:
        print('%s感谢您的配合！' % name)
