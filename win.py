import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext
import os

data = {"script":""}

window = tk.Tk()
# 设置窗口大小
winWidth = 800
winHeight = 600
# 获取屏幕分辨率
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
 
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
 
# 设置主窗口标题
window.title("lby")
# 设置窗口初始位置在屏幕居中
window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# 设置窗口图标
# window.iconbitmap("./image/icon.ico")
# 设置窗口宽高固定
# window.resizable(0, 0)
 
# 定义列的名称
tree = ttk.Treeview(window, show = "tree")
 
myid=tree.insert("",0,"文本操作",text="文本操作",values=(""))  # ""表示父节点是根
myidx1=tree.insert(myid,0,"JSON格式化",text="JSON格式化",values=("D:/python_project/my_toolbox/scripts/格式化对象.py"))  # text表示显示出的文本，values是隐藏的值
myidx2=tree.insert(myid,1,"时间格式化",text="时间格式化",values=("D:/python_project/my_toolbox/scripts/时间转换.py"))  # text表示显示出的文本，values是隐藏的值
myidx3=tree.insert(myid,1,"url编码",text="url编码",values=("D:/python_project/my_toolbox/scripts/url编码.py"))  # text表示显示出的文本，values是隐藏的值

 
# 鼠标选中一行回调
def selectTree(event):
    for item in tree.selection():
        item_text = tree.item(item, "values")
        if item_text:
            data["script"] = item_text[0]
            break



def run_cmd():
    if(data["script"]):
        input_text = text.get("1.0", tk.END)
        if input_text:
            with open('D:\\python_project\\my_toolbox\\input.txt', "w", encoding="utf-8") as f:
                f.write(input_text)
            with os.popen("python %s" % data["script"]) as f:
                out.delete("1.0", tk.END)
                out.insert("1.0", f.read())       



# 选中行
tree.bind('<ButtonRelease-1>', selectTree)
 
tree.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
frame = tk.Frame(window)
frame.pack(side=tk.RIGHT)
text = tkinter.scrolledtext.ScrolledText(frame, height=10)
text.pack(side=tk.TOP)
b = tk.Button(frame, width=20, text="运行", command=run_cmd)
b.pack(side=tk.TOP)
out = tkinter.scrolledtext.ScrolledText(frame, height=30)
out.pack(side=tk.TOP)
window.mainloop()