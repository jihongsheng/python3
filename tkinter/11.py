from tkinter import *

root = Tk()

# 获取当前根窗口的宽和高
cur_width = root.winfo_width()
cur_height = root.winfo_height()

# 获取电脑屏幕的宽、高
scn_width, scn_height = root.maxsize()

# 窗口显示的坐标拼接成固定格式字符串
tmpcnf = '+%d+%d' % ((scn_width-cur_width)/2, (scn_height-cur_height)/2)
root.geometry(tmpcnf)

# 固定窗口的长度，不可改变窗口大小（width=None, height=None)
root.resizable(False, False)

Label(root, text='我是标签', bg='yellow').pack(side=LEFT)
Button(root, text='我司按钮', bg='yellow').pack()

root.mainloop()