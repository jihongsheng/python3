from tkinter import *

root = Tk()

list_var = StringVar()
list_var.set(['Go', 'Python', 'Java', 'Php', 'Html',
              'JavaScript', 'C', 'C++++++++++++++++++++++++++++++++++++'])

# 分别创建x方向，y方向的两条滚动条，orient属性设置其滚动条的方向
y_bar = Scrollbar(root, orient=VERTICAL)
x_bar = Scrollbar(root, orient=HORIZONTAL)

# 创建列表框
list_box = Listbox(root, yscrollcommand=y_bar.set,
                   xscrollcommand=x_bar.set,
                   listvariable=list_var, height=5)

y_bar['command'] = list_box.yview
x_bar['command'] = list_box.xview

# 设置布局方位
y_bar.pack(side=RIGHT, fill=Y)
x_bar.pack(side=BOTTOM, fill=X)
list_box.pack(anchor=NW, fill=BOTH, expand=YES)

'''
# BROWSE 单选，鼠标点击向下拖，可以选择;
# SINGLE 也是单选，只能通过点击单选
# EXTENDED 多选， 鼠标点击向下拖，可以选择;
# MULTIPLE 多选， 只能通过点击多选

Listbox(root, listvariable=list_var, selectmode=EXTENDED).pack()
'''
root.mainloop()