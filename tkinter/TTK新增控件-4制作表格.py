import tkinter as tk
from tkinter import ttk


def item_select(event):
    for select in tree.selection():
        print(tree.item(select, "values"))


def head_onclick(type):
    print(type)


root = tk.Tk()

# show 用于禁止列顶部标签， columns用于设置每一列的列标识字符串
#  show='headings'  做表格必须隐藏第一列代码
tree = ttk.Treeview(root, show='headings', columns=['0', '1', '2'])

# 监听tree中item被选中的事件
tree.bind("<<TreeviewSelect>>", item_select)

# 设置表头名称
tree.heading(0, text='序号', command=lambda: head_onclick('序号'))
tree.heading(1, text='姓名', command=lambda: head_onclick('姓名'))
tree.heading(2, text='年龄', command=lambda: head_onclick('年龄'))

#  设置每个元素的样式
tree.column(0, anchor='center')
tree.column(1, anchor='center')
tree.column(2, anchor='center')

# “end”标识往父节点的最后一个位置插入
item1 = tree.insert("", "end", values=("1", "张三", "19"))
item1 = tree.insert("", "end", values=("2", "李四", "20"))
item1 = tree.insert("", "end", values=("3", "王五", "21"))
item1 = tree.insert("", "end", values=("4", "赵六", "21"))

tree.pack()
root.mainloop()
