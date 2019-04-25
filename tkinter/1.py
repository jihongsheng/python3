import tkinter as tk
"""
事件和回调
def onclick():
    print("我被点击了")
# 创建一个按钮
btn = tk.Button(root, text="点我啊", command=onclick)
btn.pack()
"""


def onclick():
    print("我被点击了")

root = tk.Tk()

label_1 = tk.Label(root, text="这是一个标签")
label_1.pack()

# 创建一个按钮
btn = tk.Button(root, text="点我啊", command=onclick)
btn.pack()

root.mainloop()
