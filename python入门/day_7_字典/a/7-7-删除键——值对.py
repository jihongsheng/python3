# -*- coding: UTF-8 -*-
# 对于字典中不再需要的信息，可使用del 语句将相应的键—值对彻底删除。使用del 语句时，必须
# 指定字典名和要删除的键。例如，下面的代码从字典alien_0 中删除键'points' 及其值：
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# 代码行让Python将键'points' 从字典alien_0 中删除，同时删除与这个键相关联的值
del alien_0['points']   # ❶
print(alien_0)
# 输出表明，键'points' 及其值5 已从字典中删除，但其他键—值对未受影响：



