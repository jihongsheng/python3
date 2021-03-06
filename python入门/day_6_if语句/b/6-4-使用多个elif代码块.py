# -*- coding: UTF-8 -*-

# 可根据需要使用任意数量的elif 代码块，例如，假设前述游乐场要给老年人打折，可再添加一个条件测试，
# 判断顾客是否符合打折条件。下面假设对于65岁（含）以上的老人，可以半价（即5美元）购买门票：
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:  # ❶
    price = 10
else:   # ❷
    price = 5
print("Your admission cost is $%s. " % price)
# 这些代码大都未变。第二个elif 代码块（见❶）通过检查确定年龄不到65岁后，才将门票价格设
# 置为全票价格——10美元。请注意，在else 代码块（见❷）中，必须将所赋的值改为5，因为仅
# 当年龄超过65（含）时，才会执行这个代码块。



