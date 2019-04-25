from tkinter import *

root = Tk()

# grid布局实现

Label(text="label_1:").grid()
Entry().grid(row=0, column=1)

Label(width=25, height=3, bg="yellow").grid(row=0, column=2, columnspan=2, rowspan=2)

Label(text="label_2:").grid(row=1)
Entry().grid(row=1, column=1)

Checkbutton(text="选择我").grid(column=0, columnspan=2, sticky="w")

Button(text="btn_1").grid(row=2, column=2, sticky="ew")
Button(text="btn_2").grid(row=2,column=3, sticky="ew")

# pack 布局
"""

left = Frame(root)
left.pack(side="left", fill="both", expand="yes")
right = Frame(root)
right.pack(side="left", fill="both", expand="yes")

#  左边
one_row = Frame(left)
Label(one_row, text="label_1").pack(side="left")
Entry(one_row).pack(side="left")
one_row.pack()

tow_row = Frame(left)
Label(tow_row, text="label_2").pack(side="left")
Entry(tow_row).pack(side="left")
tow_row.pack()

Checkbutton(left, text="选择我").pack(anchor="w")

# 右边
Label(right, width=25, height=3, bg="yellow").pack()

bottom = Frame(right)

Button(bottom, text="btn1").pack(side="left", fill="x", expand="yes")
Button(bottom, text="btn2").pack(side="left", fill="x", expand="yes")
bottom.pack(fill="x")
"""

root.mainloop()