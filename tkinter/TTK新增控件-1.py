import tkinter as tk
import tkinter.ttk as ttk

"""
ttk 新增6个控件，这里主要介绍4个重要的
- Combobox  输入框下拉选项菜单
- Progressbar 进度条控件
"""

root = tk.Tk()
ttk.Label(root, text="编程语言").pack(side=tk.LEFT, padx=5, pady=5)

combo = ttk.Combobox(root, values=['Go', 'Python', 'Java', 'C++'])
# 设置当前选中的项
combo.current(1)
combo.pack(side=tk.LEFT, padx=5, pady=5)

# 创建进度条控件
# mode='indeterminate' 回弹效果
progress = ttk.Progressbar(root, mode='indeterminate', length=100)
progress.pack(padx=10, pady=10)
# 启动进度条控件
progress.start()

# mode='determinate'  直线效果
progress2 = ttk.Progressbar(root, mode='determinate', length=100)
progress2.pack(padx=10, pady=10)
progress2.start()

root.mainloop()
