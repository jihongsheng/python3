import tkinter as tk

root = tk.Tk()
# left -左对齐；right -右对齐； top - 上；bottom - 下
# expand 要求但不使用的空间；fill要求并使用的空间
tk.Button(root, text='A').pack(side=tk.RIGHT, ipady=1)
tk.Button(root, text='B').pack(side=tk.RIGHT, ipady=1)
tk.Button(root, text='C').pack(side=tk.RIGHT, ipady=1)


root.mainloop()
"""
import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)

tk.Label(frame, text="Pack 布局的 side 和 file", bg="red").pack()
tk.Button(frame, text="A").pack(side=tk.LEFT, fill=tk.Y)
tk.Button(frame, text="B").pack(side=tk.TOP, fill=tk.X)     # TOP 上   BOTTOM 下
tk.Button(frame, text="C").pack(side=tk.RIGHT, fill=tk.NONE)
tk.Button(frame, text="D").pack(side=tk.TOP, fill=tk.BOTH)

# 需注意，顶部框架不会展开，也不会填充X或Y方向
frame.pack()

tk.Label(root, text="Pack 布局的 expand").pack()
tk.Button(root, text="我不扩展").pack()
tk.Button(root, text="我不向x方向填充，但我扩展").pack(expand=1)
tk.Button(root, text="我向x方向填充，而且我扩展").pack(expand=1, fill=tk.X)

root.mainloop()
"""

"""
import tkinter as tk

root = tk.Tk()

# tk.Label(root, text="这是一个标签", bg="red").pack()
# tk.Label(root, text="这是一个标签", bg="blue").pack()
fill 取值为x,y,both,none; both是x,y轴都占满
tk.Button(root, text='a').pack(side=tk.LEFT, expand=1, fill='both')
tk.Button(root, text='b').pack(side=tk.LEFT, expand=1, fill='both')
tk.Button(root, text='c').pack(side=tk.LEFT, expand=1, fill='both')

root.mainloop()
"""


"""
import tkinter as tk

root = tk.Tk()

f1 = tk.Frame(root)
f2 = tk.Frame(root)

tk.Label(f1, text='左1').pack()
tk.Label(f1, text='左2').pack()
tk.Label(f1, text='左3').pack()

tk.Button(f2, text='右1').pack(side="left", padx=10)
tk.Button(f2, text='右1').pack(side="left", ipadx=10)
tk.Button(f2, text='右1').pack(side="left")

f1.pack(side="left")
f2.pack(side="left")

root.mainloop()
"""