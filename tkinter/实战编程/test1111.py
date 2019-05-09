from tkinter import *
from tkinter import messagebox

class LoginPage:
    """登录界面"""

    def __init__(self, master):
        self.root = master
        self.root.geometry('400x200+600+400')
        self.root.title('上传服务器')
        self.username = StringVar()
        self.password = StringVar()
        self.page = Frame(self.root)
        self.creatapage()

    def creatapage(self):
        """界面布局"""
        Label(self.page).grid(row=0)
        Label(self.page, text='请输入IP地址:').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='请输入服务器密码:').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, stick=E, column=1)
        Label(self.page, text='请输入数据库密码:').grid(row=3, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=3, stick=E, column=1)
        Label(self.page, text='请输入大区名称:').grid(row=4, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=4, column=1, stick=E)
        self.page.pack()


if __name__ == '__main__':
    root = Tk()
    LoginPage(root)
    root.mainloop()
