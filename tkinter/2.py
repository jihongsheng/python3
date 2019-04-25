import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# img = Image.open("image/0.jpg")
# photo = ImageTk.PhotoImage(img)
#
# tk.Label(root, text="文字").pack()
# # 插入图片
# tk.Label(root, image=photo).pack()


def click1():
    global val
    print("您输入的是", val.get())

def click():
    global int_val
    print("您选择的是", int_val.get())
# 多选
# tk.Checkbutton(root, text="唱歌", command=click).pack()
# tk.Checkbutton(root, text="跳舞", command=click).pack()
# 单选
int_val = tk.IntVar()
tk.Radiobutton(root, text="男", variable=int_val, value=1, command=click).pack()
tk.Radiobutton(root, text="女", variable=int_val, value=2, command=click).pack()

# Entry 单行文本框
val = tk.StringVar()
val.set("请输入...")
# tk.Entry(root, textvariable=val).pack()
# tk.Entry(root, show="*").pack()

tk.Entry(root, textvariable=val).pack()

tk.Button(root, text="获取", command=click1).pack()
# # 水平方向-范围, tickinterval=50 显示刻度 length=空间长度， from_=其实值，to=结束值
# tk.Scale(root, orient=tk.HORIZONTAL, from_=0, to=80, tickinterval=20, length = 200).pack()
# # 垂直方向
# tk.Scale(root, orient=tk.VERTICAL).pack()




root.mainloop()
