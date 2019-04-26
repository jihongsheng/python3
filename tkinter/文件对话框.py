from tkinter import *
from tkinter import filedialog


def onclick():
    # 打开文件对话框
    file_name = filedialog.askopenfilename(
        title='打开我的文件', initialdir="D:\\",
        filetypes=[("PNG", ".png"), ("文本文档", '.txt')]
    )
    print(file_name)


def save_file():
    # 保存文件对话框
    file_name = filedialog.asksaveasfilename(
        title="保存文件", initialdir="D:\\",
        filetypes=[("Python", ".py"), ("文本文档", '.txt')]
    )
    print(file_name)


def folder():
    # 选择文件夹对话框
    file_name = filedialog.askdirectory(initialdir="D:\\")
    print(file_name)


root = Tk()

Button(root, text='浏览', command=onclick).pack()
Button(root, text="保存", command=save_file).pack()
Button(root, text="选择文件夹", command=folder).pack()
root.mainloop()
