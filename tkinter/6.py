import tkinter as tk


def callback(a):
    print("我被点击了", a.get())


def create_view():
    val = tk.StringVar()
    tk.Entry(root, textvariable=val).pack()
    tk.Button(root, text="btn", command=lambda: callback(val)).pack()

# 命令事件
root = tk.Tk()
create_view()

root.mainloop()

# lambda 是匿名函数
# add = lambda x, y: x + y
# print(add(8, 10))
