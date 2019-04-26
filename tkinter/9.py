from tkinter import *

content = "孤山寺北贾亭西，水面初平云脚低。几处早莺争暖树，谁家新燕啄春泥。\
　　          乱花渐欲迷人眼，浅草才能没马蹄。最爱湖东行不足，绿杨阴里白沙堤。"


def touch(event):       # 获取鼠标索引
    print(text_area.index(CURRENT))
    print(text_area.get(CURRENT, END))


# 清空
def clear():
    text_area.delete('1.0', END)

root = Tk()

# 创建垂直滚动条
y_bar = Scrollbar(root, orient=VERTICAL)
y_bar.pack(side=RIGHT, fill=Y)

text_area = Text(root, yscrollcommand=y_bar.set, wrap=WORD)
y_bar['command'] = text_area.yview

# 获取鼠标索引
text_area.bind('<Motion>', touch)
text_area.pack()

# 插入文本内容
# END 插到文本最后一行
text_area.insert(INSERT, content)
# 1.0 表示第一行，开始的位子
# text_area.insert('1.0', '这是一句xxx话')
# 1.0+5c是表示第一行从0开始偏移5个位置
# text_area.insert('1.0+10c', '这是一句xxx话')

# 创建一个mark
text_area.mark_set('xxx', '1.5')
# 在名为“xxx”的mark处插入文本，第三参数为插入的文本设置一个名为"here_red"的tag
text_area.insert("xxx", "这是一句XXX话", "here_red")     # 增加here_red

# 设置Tag的样式
text_area.tag_config("here_red", foreground='red')
# 创建指定范围的Tag
text_area.tag_add("high_light", "1.50", "1.end")
text_area.tag_config("high_light", background="yellow")


# 插入图片
photo = PhotoImage(file='image/ins.gif')
text_area.image_create(END, image=photo)

# 插入控件
btn = Button(text_area, text='点我', command=clear)
text_area.window_create(END, window=btn)

root.mainloop()














