from tkinter import *

content = "　孤山寺北贾亭西，水面初平云脚低。几处早莺争暖树，谁家新燕啄春泥。\
　　          乱花渐欲迷人眼，浅草才能没马蹄。最爱湖东行不足，绿杨阴里白沙堤。"

root = Tk()
root.geometry("300x400")

# LabelFrame
top = LabelFrame(root, text='这是 Label')
top.pack(padx=8, pady=8, ipadx=5, ipady=5)

# 创建一个Label
Label(top, text=content, bg='yellow').pack()

bottom = LabelFrame(root, text='这是 Message')
bottom.pack(padx=8, pady=8)

# 创建一个Message
Message(bottom, text=content, bg='blue').pack()

# 下拉菜单
op_list = ['选项1', '选项2', '选项3']
val = StringVar()
val.set(op_list[0])
# 注意：传入的列表前需要加一个*号，这表示不定参的传递
# 两个*则表示字典类型的不定参传递
OptionMenu(root, val, *op_list).pack()

# 制定数字范围
var_range = StringVar()
var_range.set(0)
Spinbox(root, textvariable=var_range, from_=-10, to=10).pack()

# 指定列表范围
Spinbox(root, value=op_list).pack()

root.mainloop()






