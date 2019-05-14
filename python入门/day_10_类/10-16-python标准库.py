# -*- coding: UTF-8 -*-
"""
python标准库是一组模块，安装的python都包含它，你现在对类的工作原理已有大致的了解，可以开始使用其他
程序员编写好的模块了，可以使用标准库中的任何函数和类，为此只需要在程序开头包含一条简单的import语句，
下面来看看模块collections中的一个类-OrderedDict

字典让你能够将信息关联起来，但他们不记录你添加键-值对应顺序，要创建字典并记录其中的键—值对的添加顺序
，可使用模块collections 中的OrderedDict类。OrderedDict 实例的行为几乎与字典相同，区别只在于
记录了键—值对的添加顺序
"""

# 我们首先从模块collections 中导入了OrderedDict 类
from collections import OrderedDict

# 我们创建了OrderedDict 类的一个实例，并将其存储到favorite_languages 中。请注意，这里没有使
# 用花括号，而是调用OrderedDict() 来创建一个空的有序字典，并将其存储在favorite_languages 中。
favorite_languages = OrderedDict()

# 接下来，我们以每次一对的方式添加名字—语言对
favorite_languages['李四'] = 'python'
favorite_languages['王五'] = 'c'
favorite_languages['赵六'] = 'java'
favorite_languages['宋七'] = 'python'

# 我们遍历favorite_languages ，但知道将以添加的顺序获取调查结果：
for key, value in favorite_languages.items():
    print("%s 喜欢的语言是%s" % (key, value.title()))

# 这是一个很不错的类，它兼具列表和字典的主要优点（在将信息关联起来的同时保留原来的顺序）。等你开始对
# 关心的现实情形建模时，可能会发现有序字典正好能够满足需求。随着你对标准库的了解越来越深入，将熟悉大
# 量可帮助你处理常见情形的模块。注意 　你还可以从其他地方下载外部模块。本书第二部分的每个项目都需要
# 使用外部模块，届时你将看到很多这样的示例。
# 　
