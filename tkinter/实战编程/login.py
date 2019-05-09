# -*- coding: UTF-8 -*-

import pymysql
from tkinter import *


try:
    from ttk import Entry, Button
except ImportError:
    pass

class Login(object):
    def __init__(self):
        self.root = Tk()
        self.root.title(u'登录')
        self.root.resizable(False, False)
        self.root.geometry('+450+250')
        # self.sysfont = font(self.root, size=15)
        self.lb_user = Label(self.root, text=u'用户名：',width = 20,height = 10,font=("黑体", 15, "bold"))
        self.lb_passwd1 = Label(self.root, text=u'')
        self.lb_passwd = Label(self.root, text=u'密码：',width = 20,height = 5,font=("黑体", 15, "bold"))
        self.lb_user.grid(row=0, column=0, sticky=W)
        self.lb_passwd1.grid(row=1, column=0, sticky=W)
        self.lb_passwd.grid(row=2, column=0, sticky=W)

        self.en_user = Entry(self.root, width=24)
        self.en_passwd = Entry(self.root,  width=24)
        self.en_user.grid(row=0, column=1, columnspan=1)
        self.en_passwd.grid(row=2, column=1, columnspan=1)
        self.en_user.insert(0, u'请输入用户名')
        self.en_passwd.insert(0, u'请输入密码')
        self.en_user.config(validate='focusin',
                            validatecommand=lambda: self.validate_func('self.en_user'),
                            invalidcommand=lambda: self.invalid_func('self.en_user'))
        self.en_passwd.config(validate='focusin',
                              validatecommand=lambda: self.validate_func('self.en_passwd'),
                              invalidcommand=lambda: self.invalid_func('self.en_passwd'))

        self.var = IntVar()
        self.ckb = Checkbutton(self.root, text=u'记住用户名和密码', underline=0,
                               variable=self.var,font=(15))
        self.ckb.grid(row=3, column=0)
        self.bt_print = Button(self.root, text=u'登陆')
        self.bt_print.grid(row=3, column=1, sticky=E, pady=50,padx = 10)
        self.bt_print.config(command=self.print_info)

        self.bt_register = Button(self.root, text=u'注册')
        self.bt_register.grid(row=3, column=2, sticky=E, pady=50, padx=50)
        # self.bt_register.config(command=self.register_info)
        # self.root.bind('<Return>', self.enter_print)
        self.root.mainloop()

    def validate_func(self, en):
        return False if eval(en).get().strip() != '' else True

    def invalid_func(self, en):
        value = eval(en).get().strip()
        if value == u'输入用户名' or value == u'输入密码':
            eval(en).delete(0, END)
        if en == 'self.en_passwd':
            eval(en).config(show='*')

    def print_info(self):
        en1_value = self.en_user.get().strip()
        en2_value = self.en_passwd.get().strip()
        txt = u'''用户名: %s \n密码  : %s ''' % (self.en_user.get(), self.en_passwd.get())
        if en1_value == '' or en1_value == u'输入用户名':
            print(u'无用户名', u'请输入用户名')
        elif en2_value == '' or en2_value == u'输入密码':
            print(u'无密码', u'请输入密码')
        else:
            a = 0
            # 打开数据库连接
            db = pymysql.connect("62.234.41.135", "root", "root", "book")
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # SQL 查询语句
            sql = "select * from user"
            try:
                # 执行SQL语句
                cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                for row in results:
                    id = row[0]
                    name = row[1]
                    pwd = row[2]
                    if name == en1_value and pwd == en2_value:
                        a = 1
                        print ("数据库连接及验证成功！！！")
                        print ('登陆成功！！！', txt)
                    # # 打印结果
                    # print "id=%d,name=%s,pwd=%s" % \
                    #       (id, name, pwd)
            except:
                print ("Error: unable b_while fecth data")

            # 关闭数据库连接
            db.close()
            if(a == 0):
                print('用户名或密码错误！！！', txt)

    def register_info(self):
        self.rootR = Tk()
        loginPage(self.rootR)
        self.root.withdraw()

    def enter_print(self, event):
        self.print_info()

if __name__ == "__main__":
    Login()