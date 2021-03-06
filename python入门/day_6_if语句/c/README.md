# 动手试一试
- 1 以特殊方式跟管理员打招呼 ：创建一个至少包含5个用户名的列表，且其中一个用户名为'admin' 。想象你要编写代码，在每位用户登录网站后都打印一条问
候消息。遍历用户名列表，并向每位用户打印一条问候消息。
    - 如果用户名为'admin' ，就打印一条特殊的问候消息，如“Hello admin, would you like to see a status report?”。
    - 否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again”。
- 2 处理没有用户的情形 ：在为完成练习5-8编写的程序中，添加一条if 语句，检查用户名列表是否为空。
    - 如果为空，就打印消息“We need to find some users!”。
    - 删除列表中的所有用户名，确定将打印正确的消息。
- 3 检查用户名 ：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
    - 创建一个至少包含5个用户名的列表，并将其命名为current_users 。
    -  再创建一个包含5个用户名的列表，将其命名为new_users ，并确保其中有一两个用户名也包含在列表current_users 中。
    - 遍历列表new_users ，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指
出这个用户名未被使用。
    - 确保比较时不区分大消息；换句话说，如果用户名'John' 已被使用，应拒绝用户名'JOHN' 。
   
- 序数 ：序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
    - 在一个列表中存储数字1~9。
    - 遍历这个列表。
    - 在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输出内容应为1st 、2nd 、3rd 、4th 、5th 、6th 、7th 、8th 和9th ，但每个序
数都独占一行。
# 设置if 语句的格式
- 本章的每个示例都展示了良好的格式设置习惯。在条件测试的格式设置方面，PEP 8提供的唯一建议是，在诸如== 、>= 和<= 等比较运算符两边各添加一个空格，例如，if
age < 4: 要比if age<4: 好。
- 这样的空格不会影响Python对代码的解读，而只是让代码阅读起来更容易。
动手试一试
5-12 设置if 语句的格式 ：审核你在本章编写的程序，确保正确地设置了条件测试的格式。
5-13 自己的想法 ：与刚拿起本书时相比，现在你是一名能力更强的程序员了。鉴于你对如何在程序中模拟现实情形有了更深入的认识，你可以考虑使用程序来解决一
些问题。随着编程技能不断提高，你可能想解决一些问题，请将这方面的想法记录下来。想想你可能想编写的游戏、想研究的数据集以及想创建的Web应用程序。

#　小结
在本章中，你学习了如何编写结果要么为Ture 要么为False 的条件测试。你学习了如何编写简单的if 语句、if-else 语句和if-elif-else 结构。在程序中，你使用了这
些结构来测试特定的条件，以确定这些条件是否满足。你学习了如何在利用高效的for 循环的同时，以不同于其他元素的方式对特定的列表元素进行处理。你还再次学习了
Python就代码格式方面提出的建议，这可确保即便你编写的程序越来越复杂，其代码依然易于阅读和理解。
在第6章，你将学习Python字典。字典类似于列表，但让你能够将不同的信息关联起来。你将学习如何创建和遍历字典，以及如何将字典同列表和if 语句结合起来使用。学习字典
让你能够模拟更多现实世界的情形。