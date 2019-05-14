# -*- coding: UTF-8 -*-
from car import Car     # 1

my_new_car = Car('奥迪', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 1处的import 语句让Python打开模块car ，并导入其中的Car 类。这样我们就可以使用Car 类了，
# 就像它是在这个文件中定义的一样。输出与我们在前面看到的一样：

# 导入类是一种有效的编程方式。如果在这个程序中包含了整个Car 类，它该有多长呀！通过将这个类移
# 到一个模块中，并导入该模块，你依然可以使用其所有功能，但主程序文件变得整洁而易于阅读了。这
# 还能让你将大部分逻辑存储在独立的文件中；确定类像你希望的那样工作后，你就可以不管这些文件，
# 而专注于主程序的高级逻辑了。
