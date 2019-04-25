import tkinter as tk

root = tk.Tk()
tk.Label(root, text="账号:", bg="red").grid(row=0, sticky="ew")
# tk.Label(root, text="密码:").grid(row=1, sticky=tk.W)
tk.Label(root, text="密码:").grid(sticky=tk.W)

tk.Entry(root).grid(row=0, column=1, sticky="ew")
tk.Entry(root).grid(row=1, column=1, sticky=tk.E)

# columnspan=2 合并单元格;sticky="ew" 按钮拉伸
tk.Button(root, text="登录").grid(row=2, column=0, columnspan=2, sticky="ew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.mainloop()
# from tkinter import *
#
# root = Tk()
#
# Label(root, width=15, height=3, bg='red').grid(row=0, column=0)
# Label(root, width=15, height=3, bg='green').grid(row=0, column=1)
# Label(root, width=15, height=3, bg='blue').grid(row=0, column=2)
# Label(root, width=15, height=3, bg='white').grid(row=1, column=0)
# Label(root, width=15, height=3, bg='black').grid(row=1, column=1)
# Label(root, width=15, height=3, bg='grey').grid(row=1, column=2)
#
# root.mainloop()
