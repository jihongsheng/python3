from tkinter import *

content = "　孤山寺北贾亭西，水面初平云脚低。几处早莺争暖树，谁家新燕啄春泥。\
　　          乱花渐欲迷人眼，浅草才能没马蹄。最爱湖东行不足，绿杨阴里白沙堤。"


def touch(event):
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

# text_area.bind('<Motion>', touch)
text_area.pack()

# 插入文本内容
text_area.insert(INSERT, content)
text_area.insert('1.0', '这是一句xxx话')

# 插入图片
# photo = PhotoImage(file='img.gif')
# text_area.image_create(END, image=photo)

# 插入控件
btn = Button(text_area, text='点我', command=clear)
text_area.window_create(END, window=btn)

root.mainloop()














