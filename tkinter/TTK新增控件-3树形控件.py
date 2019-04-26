"""
- Treeview 树形控件
"""
import tkinter as tk
from tkinter import ttk


def item_select(event):
    for select in tree.selection():
        print(tree.item(select, 'text'))


root = tk.Tk()
# show='tree'   可以去掉标签栏
# tree = ttk.Treeview(root, show='tree')
tree = ttk.Treeview(root)

# 监听tree中item被选中的事件
tree.bind("<<TreeviewSelect>>", item_select)

# 第一个参数为父节点，第二个为此项在父节点的位置（父节点为空时，默认为根节点）
item1 = tree.insert("", 0, text="广大省")

# 在第一个节点中插入子节点
tree.insert(item1, 0, text="广州市")
tree.insert(item1, 1, text="深圳市")

item2 = tree.insert("", 0, text="陕西省")
tree.insert(item2, 0, text="西安市")
tree.insert(item2, 1, text="咸阳市")

tree.pack()
root.mainloop()
