from tkinter import *
# 增加如下导包语句即可
from tkinter.ttk import *


class App:
    def __init__(self, root):
        self.root = root
        self.set_window()
        self.create_top()
        self.create_body()
        self.create_bottom()

    # 设置窗口
    def set_window(self):
        self.root.title("测试")
        self.root.resizable(False, False)
        self.root.geometry("300x300")

    # 创建顶部
    def create_top(self):
        Label(self.root, text='Top').pack()

    # 创建主体
    def create_body(self):
        self.input = StringVar()
        Entry(self.root, textvariable=self.input).pack()

    # 创建底部
    def create_bottom(self):
        Button(self.root, text='Bottom', command=self.onclick).pack()

    # 按钮回调函数
    def onclick(self):
        print(self.input.get())


if __name__ == "__main__":
    root = Tk()
    App(root)
    root.mainloop()

