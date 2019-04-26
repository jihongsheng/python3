from tkinter import *


def test(window):
    # 让窗口最小化
    window.iconify()
    # 将最小化的窗口显示出来
    # window.deiconify()

    # 销毁窗口
    # window.destroy()
    # 退出mainloop循环
    # window.quit()

def onclick():
    '''Toplevel打开新窗口'''
    window = Toplevel()
    # 设置窗口出现的位置
    window.geometry("+300+300")
    window.title("子窗口")
    # 固定窗口的长宽，不可改变窗口的大小（width=None,hefght=None）
    window.resizable(False, False)

    # 该方法传入True时，去除窗口边框
    # window.overrideredirect(True)
    Button(window, text="点你妹", command=lambda: test(window)).pack()

    # 设置它所依托的父窗口
    window.transient(root)
    # 必须调用mainloop,打开一个新窗口后，需要进入新窗口的事件循环
    window.mainloop()

root = Tk()

# 设置窗口标题
root.title("主窗口")

# 设置窗口的宽高与显示的位置
root.geometry("300x200+200+200")

# 获取当前根窗口的宽和高
cur_width = root.winfo_width()
cur_height = root.winfo_height()

# 获取电脑屏幕的宽、高
scn_width, scn_height = root.maxsize()

# 窗口显示的坐标拼接成固定格式字符串
tmpcnf = '+%d+%d' % ((scn_width-cur_width)/2, (scn_height-cur_height)/2)
root.geometry(tmpcnf)

# 固定窗口的长宽，不可改变窗口的大小（width=None,hefght=None）
root.resizable(False, False)

# 设置窗口小图标（必须位于geometry与resizable方法之后）
root.iconbitmap("image/2.ico")

Button(root, text='打开窗口', command=onclick).pack()
# root.overrideredirect(True)   # 去边框
root.mainloop()

"""
def onclick():
    '''Toplevel打开新窗口'''
    window = Toplevel()
    Label(window, text='我是新窗口').pack()

    # 设置它所依托的父窗口
    window.transient(root)
    # 必须调用mainloop,打开一个新窗口后，需要进入新窗口的事件循环
    window.mainloop()


root = Tk()
Button(root, text='打开窗口', command=onclick).pack()

root.mainloop()
"""
