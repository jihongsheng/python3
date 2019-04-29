from tkinter import *
from tkinter.ttk import *


class App(Tk):
    def __init__(self):
        super().__init__()

        self.set_window()
        self.create_top()
        self.create_body()
        self.create_bottom()

    # 设置窗口
    def set_window(self):
        """
        :geometry   设置主窗口宽和高
        :title  主窗口标题
        :resizable  固定主窗口大小，不能随意拖动
        """
        self.geometry("800x600+200+200")
        self.title("联系测试")
        self.resizable(False, False)

    # 创建顶部
    def create_top(self):
        Label(self, text='Top').grid(row=0, column=0)

    # 创建主体
    def create_body(self):
        self.input = StringVar()
        Entry(self, textvariable=self.input).grid(row=0, column=1)

    # 创建底部
    def create_bottom(self):
        Button(self, text='Bottom', command=self.onclick).grid(row=1, column=0)

    # 按钮回调函数
    def onclick(self):
        print(self.input.get())


if __name__ == '__main__':
    app = App()
    app.mainloop()


