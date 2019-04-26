from tkinter import *


def a():
    print(my_entry.get())
    return


root = Tk()
# Label(root, text="Please input a number:").pack(side=LEFT)
# Entry(root).pack(side=RIGHT)
# Button(root, text='print_entry',command=a).pack(side=BOTTOM)
my_entry = Entry(root)
my_entry.pack(side=LEFT)


Button(root, text='print_entry', command=a).pack(side=BOTTOM)
root.mainloop()
