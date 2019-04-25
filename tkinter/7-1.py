import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.set_window()
        self.create_top()
        self.create_body()
        self.create_bottom()

    # 设置窗口
    def set_window(self):
        self.title("测试")
        self.resizable(False, False)

    # 创建顶部
    def create_top(self):
        tk.Label(self, text='Top').pack()

    # 创建主体
    def create_body(self):
        self.input = tk.StringVar()
        tk.Entry(self, textvariable=self.input).pack()

    # 创建底部
    def create_bottom(self):
        tk.Button(self, text='Bottom', command=self.onclick).pack()

    # 按钮回调函数
    def onclick(self):
        print(self.input.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()

