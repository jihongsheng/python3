from tkinter import *
from tkinter.ttk import *
import pymysql


class Login:
    """登录界面"""
    def __init__(self, master):
        self.root = master
        self.root.geometry('320x180+200+200')
        self.root.title('测试登录数据库')
        self.username = StringVar()
        self.password = StringVar()
        self.page = Frame(self.root)
        self.creatapage()
        # self.login()

    def creatapage(self):
        """界面布局"""
        Label(self.page).grid(row=0)
        Label(self.page, text='用户名:').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码:').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password,show='*').grid(row=2, stick=E, column=1)
        Button(self.page, text='登录', command=self.login).grid(row=3, stick=W, pady=10)
        # Button(self.page, text='注册账号').grid(row=3, stick=E, column=1)
        self.page.pack()

    def login(self):
        """登录功能
         # 参数依次是：IP地址,数据库登录名，数据库密码，数据库实体名称,指定字符集 （未指定可能出现中文乱码）
        IP：62.234.41.135
        密码：xymail2016!
        :return:
        """
        try:
            db = pymysql.connect(host=self.username.get(), user='root', password=self.password.get(), port=3306)
            print("连接Mysql数据库成功")
        except:
            print("无法连接到MySQL数据库")
            exit()

        # 使用cursor() 方法创建一个游标对象 cursor
        # cursor = db.cursor()
        # cursor.execute('SELECT VERSION()')
        # data = cursor.fetchone()
        # print('Database version:', data)
        # db.close()


if __name__ == '__main__':
    root = Tk()
    Login(root)
    root.mainloop()
