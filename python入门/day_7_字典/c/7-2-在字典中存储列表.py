# -*- coding: UTF-8 -*-
# 有时候，需要将列表存储在字典中，而不是将字典存储在列表中。例如，你如何描述顾客点的比萨呢？
# 如果使用列表，只能存储要添加的比萨配料；但如果使用字典，就不仅可在其中包含配料列表，还可包
# 含其他有关比萨的描述。
# 在下面的示例中，存储了比萨的两方面信息：外皮类型和配料列表。其中的配料列表是一个与键'toppings'
# 相关联的值。要访问该列表，我们使用字典名和键'toppings'，就像访问字典中的其他值一样。这将返回
# 一个配料列表，而不是单个值：

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print('You ordered a_input %s-crust pizza with the following toppings:' % pizza['crust'])

for topping in pizza['toppings']:
    print("\t %s" % topping)


like_name = {
    '张三': ['python', 'go'],
    '李四': ['java'],
    '王五': ['c#', 'c'],
    '赵六': ['shell', 'php'],
}

for name, languages in like_name.items():
    print("\n%s's favorite languages are:" % name.title())
    for language in languages:
        print("\t%s" % language.title())
