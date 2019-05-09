from tkinter import *
from tkinter.ttk import *
import pymysql


def sign_in():
    IP = my_entry.get()
    # print(IP)
    Mysql_Pass = my_passwd.get()
    # print(Mysql_Pass)
    db = pymysql.connect(host=IP, user='root', password=Mysql_Pass, port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print('Database version:', data)
    db.close()


root = Tk()
Label(root, text="IP:").grid(row=0, sticky="ew")
my_entry = Entry(root)
my_entry.grid(row=0, column=1, sticky="ew")
Label(root, text="密码:").grid(row=1, sticky="ew")
# my_passwd = Entry(root).grid(row=1, column=1, sticky="ew")
my_passwd = Entry(root)
my_passwd.grid(row=1, column=1, sticky="ew")
Button(root, text="登录", command=sign_in).grid(row=2, column=0, columnspan=2, sticky="ew")
root.mainloop()



# from tkinter import *
# import pymysql
#
#
# def sign_in():
#     IP = my_entry.get()
#     print(IP)
#     # db = pymysql.connect(host=IP, user='root', password=Mysql_Pass, port=3306)
#     # pass
#
# root = Tk()
# my_entry = Entry(root)
# my_entry.grid()
# # Button(root, text='print_entry', command=sign_in).pack(side=BOTTOM)
# Button(root, text="登录", command=sign_in).grid(row=2, column=0, columnspan=2, sticky="ew")
#
# # db = pymysql.connect(host=IP, user='root', password=Mysql_Pass, port=3306)
# root.mainloop()



"""
from tkinter import *
import pymysql


def sign_in():
    IP = my_entry.get()
    print(IP)
    Mysql_Pass = my_passwd.get()
    print(Mysql_Pass)
    # db = pymysql.connect(host=IP, user='root', password=Mysql_Pass, port=3306)


root = Tk()
Label(root, text="IP:", bg="yellow").grid(row=0, sticky="ew")
my_entry = Entry(root).grid(row=0, column=1, sticky="ew")
Label(root, text="密码:", bg="yellow").grid(row=1, sticky="ew")
my_passwd = Entry(root).grid(row=1, column=1, sticky="ew")
Button(root, text="登录", command=sign_in).grid(row=2, column=0, columnspan=2, sticky="ew")
root.mainloop()







# import tkinter as tk
#
# root = tk.Tk()
# tk.
# # tk.Label(root, text="密码:").grid(row=1, sticky=tk.W)
# tk.Label(root, text="密码:").grid(sticky=tk.W)
#
# tk.Entry(root).grid(row=0, column=1, sticky="ew")
# tk.Entry(root).grid(row=1, column=1, sticky=tk.E)
#
# # columnspan=2 合并单元格;sticky="ew" 按钮拉伸
# tk.Button(root, text="登录").grid(row=2, column=0, columnspan=2, sticky="ew")
#
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# root.mainloop()
"""