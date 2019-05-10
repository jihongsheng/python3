# -*- coding: UTF-8 -*-
# 有时候，需要禁止函数修改列表。例如，假设像前一个示例那样，你有一个未打印的设计
# 列表，并编写了一个将这些设计移到打印好的模型列表中的函数。你可能会做出这样的
# 决定：即便打印所有设计后，也要保留原来的未打印的设计列表，以供备案。但由于你
# 将所有的设计都移出了unprinted_designs ，这个列表变成了空的，原来的列表没有
# 了。为解决这个问题，可向函数传递列表的副本而不是原件；这样函数所做的任何修
# 改都只影响副本，而丝毫不影响原件。
# 要将列表的副本传递给函数，可以像下面这样做：
# function_name(list_name[:])
# 切片表示法[:] 创建列表的副本。在print_models.py中，如果不想清空未打印的设计列表，
# 可像下面这样调用print_models() ：
# print_models(unprinted_designs[:], completed_models)
# 这样函数print_models() 依然能够完成其工作，因为它获得了所有未打印的设计的名称，但它
# 使用的是列表unprinted_designs 的副本，而不是列表unprinted_designs 本身。像以前一样，
# 列表completed_models 也将包含打印好的模型的名称，但函数所做的修改不会影响到
# 列表unprinted_designs 。虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分
# 的理由需要传递副本，否则还是应该将原始列表传递给函数，因为让函数使用现成列表可避免
# 花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此。
