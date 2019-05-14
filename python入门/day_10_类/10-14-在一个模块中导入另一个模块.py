# -*- coding: UTF-8 -*-

"""
有时候，需要将类分散到多个模块中，以免模块太大，或在同一个模块中存储不相关的类。将类存储在多个模块中
时，你可能会发现一个模块中的类依赖于另一个模块中的类。
在这种情况下，可在前一个模块中导入必要的类。
例如，下面将Car 类存储在一个模块中，并将ElectricCar 和Battery 类存储在另一个模块中。我们将第二
个模块命名为electric_car.py （这将覆盖前面创建的文件electric_car.py），并将Battery 和Elec
tricCar 类复制到这个模块中：
"""
'''
electric_car.py
"""一组可用于表示电动汽车的类"""
❶ from car import Car
class Battery():
    --snip--
class ElectricCar(Car):
    --snip--
    
ElectricCar 类需要访问其父类Car ，因此在❶处，我们直接将Car 类导入该模块中。如果我们忘记了这行代码，Python将在我们试图创建ElectricCar 实例时引发错误。
我们还需要更新模块car ，使其包含Car 类：
car.py
"""一个可用于表示汽车的类"""
class Car():
    --snip--
    
现在可以分别从每个模块中导入类，以根据需要创建任何类型的汽车了：

my_cars.py
❶ from car import Car
from electric_car import ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
在❶处，我们从模块car 中导入了Car 类，并从模块electric_car 中导入ElectricCar 类。接下来，我们创建了一辆普通汽车和一辆电动汽车。这两种汽车都得以正确地
创建：
2016 Volkswagen Beetle
2016 Tesla Roadster
'''

