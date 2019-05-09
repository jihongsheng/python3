import tkinter as tk

root = tk.Tk()
tk.Label(root, text='键盘').pack()


def callback(event):
    print('EventType=', event.type)
    print('keysym=', event.keysym)

frame = tk.Frame(root, bg='khaki', width=100, height=80)
frame.pack()
root.bind("<KeyPress-a_input>", callback)   # a键
root.bind("<KeyPress-F1>", callback)   # F1键
root.bind("<Control-Alt-a_input>", callback)   # Ctrl + Alt + a键


root.mainloop()