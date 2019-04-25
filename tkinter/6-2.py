import tkinter as tk

root = tk.Tk()
tk.Label(root, text='单击').pack()


def callback(event):
    print("EventType=", event.type)
    print("Num=", event.num)


def callback1(event, a, b):
    print(a, b)
    print("EventType=", event.type)

# 注册回调时，在lambda表示中需要定义event参数

"""
<Button-1>  鼠标左击事件
<Button-2>  鼠标滚轮事件
<Button-3>  鼠标右击事件
<Double-Button-1>   鼠标左双击事件
<Triple-Button-1>   鼠标左三击事件
"""

frame = tk.Frame(root, bg='khaki', width=100, height=80)
frame.bind("<Button-1>", lambda event: callback1(event, 1, 2))
frame.pack()

root.mainloop()
