import tkinter as tk


class Command:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def callback(args):
    print("被点击了", args)



root = tk.Tk()
tk.Button(root, text="单击", command=Command(callback, "按钮")).pack()

root.mainloop()
