from tkinter import Tk
from tkinter import ttk

root = Tk()

style = ttk.Style()

# 定义一个全局样式作为默认样式("." 表示此样式将应用于顶级窗口及其所有子元素)
style.configure('.', font="Arial 14", foreground='brown', background='yellow')

# 未指定样式时，使用全局默认样式
ttk.Label(root, text='没有指定样式').pack()

# 定义一个名为danger的新样式(newName.oldName 格式)
style.configure('danger.TButton', font='Times 12', foreground='red', padding=1)
ttk.Button(root, text='我是用danger样式', style='danger.TButton').pack()

# 为小控件的不同状态指定样式
style.map('new_state_style.TButton', foreground=[('pressed', 'red'), ('active', 'blue')])
ttk.Button(text='不同状态不同样式', style='new_state_style.TButton').pack()

# 覆盖Entry的当前主题（即使没有指定样式，也会受到主题更改的影响）
current_theme = style.theme_use()
style.theme_settings(current_theme,
                     {'TEntry': {
                         'configure': {'padding': 10},
                         "map": {'foreground': [('focus', 'red')]}}})

ttk.Entry().pack()

ttk.Label(root, text="hello, world").pack()

root.mainloop()