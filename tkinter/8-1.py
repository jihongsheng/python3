from tkinter import  Tk, Menu
root = Tk()

# 创建窗口顶部的菜单栏对象
menu_bar = Menu(root)
# 将菜单栏对象设置给跟窗口
root["menu"] = menu_bar # 等价与 root.config(menu=menu_bar)

# 创建“文件” 联级菜单
file_menu = Menu(menu_bar, tearoff=0)
# 在菜单栏添加菜单标签，并将该标签与相应的联级菜单关联起来
menu_bar.add_cascade(label='文件', menu=file_menu)

# 在文件联级菜单中添加菜单项
file_menu.add_command(label='新建', accelerator='Ctrl+N')
file_menu.add_command(label='打开', accelerator='Ctrl+O')
file_menu.add_command(label='保存', accelerator='Ctrl+S')
# 添加分割线-
file_menu.add_separator()
file_menu.add_command(label='退出', accelerator='Alt+F4')

# tearoff 分离菜单
# about_menu = Menu(menu_bar)
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='关于', menu=about_menu)
about_menu.add_command(label='查看帮助')
about_menu.add_command(label='检查更新')

root.mainloop()