from tkinter import *
from tkinter.ttk import *


# 按钮回调函数
def onclick():
    global val
    print("您输入的是", val.get())


root = Tk()
root.title("我的小程序")
root.geometry("350x200")
root.resizable(False, False)

val = StringVar()
Entry(root, textvariable=val).pack()
Button(root, text='Bottom', command=onclick).pack()

root.mainloop()
