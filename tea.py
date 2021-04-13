import sys
import os
import common
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext
import tkinter.simpledialog
import shutil
import subprocess
import threading

main_path = 'D:\\python_project\\my_toolbox\\tea_main'
window = tk.Tk()
config = common.Dict()
config.exclusions = ('__pycache__', 'code-generate', 'out')

folder_img = tk.PhotoImage(file="ico/folder.png")
file_img = tk.PhotoImage(file="ico/file.png")
config.t = None


def main():
    config.tree_data = query_path_data(main_path)
    init_window()
    window.mainloop()
    

def run_command(s):
    process = subprocess.Popen("d:\\Miniconda3\\Scripts\\activate.bat & python -u %s"% s, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # process.wait()
    # command_output = process.stdout.read()
    config.output.delete("1.0", tk.END)
    while True:
        s = process.stdout.readline()
        if len(s) > 0:
        # print(command_output)
        # return command_output
            config.output.insert(tk.END, s)
        else:
            break
        


def query_path_data(path):
    if not os.path.isdir(path):
        return None

    data = common.Dict()
    with open(os.sep.join((path, 'config.txt')), 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in filter(lambda x:x, lines):
        s = line.split("=")    
        if len(s) != 2:
            print(s)
            return None
        data[s[0].strip()] = s[1].strip()
    data.path = path
    data.children = []
    for item in filter(lambda x: os.path.isdir(os.path.join(path,x)) and x not in config.exclusions, os.listdir(path)):
        children = query_path_data(os.path.join(path, item))
        data.children.append(children)
    if data['type'] == "dir":
        data.isLeaf = False
    else:
        data.isLeaf = True
    return data


def init_window():
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
    config.tree = tree
    tree.bind('<Double-1>', treeDbClick)
    tree.bind("<ButtonPress-1>",bDown)
    tree.bind("<ButtonRelease-1>",bUp)
    # tree.bind("<B1-Motion>",bMove)
    add_tree_item(tree)

    tree.pack(side = tk.LEFT, expand = True, fill = 'both')
    frame = ttk.Frame(window, width = winWidth - 10, padding='5 0')
    frame.pack(side=tk.RIGHT)
    text = tkinter.scrolledtext.ScrolledText(frame, height=10)
    text.pack(side=tk.TOP)
    
    out = tkinter.scrolledtext.ScrolledText(frame,height = winHeight - 10)
    out.pack(side=tk.BOTTOM)
    config.input = text
    config.output = out
    rclick = RightClick(window)
    tree.bind('<Button-3>', rclick.popup)
    window.bind('<F5>', refresh)

    menubar = tk.Menu(window)
    # 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
    filemenu = tk.Menu(menubar, tearoff=False)
    filemenu.add_command(label="停止运行的进程", command=stop_running_thread)
    filemenu.add_separator()
    filemenu.add_command(label="退出", command=window.quit)
    menubar.add_cascade(label="文件", menu=filemenu)
    window.config(menu=menubar)

def stop_running_thread():
    if config.t:
        common.stop_thread(config.t)
        config.t = None
        config.output.delete("1.0")
        config.output.insert(tk.END, "stop running thread ok")


def refresh(event):
    config.tree_data = query_path_data(main_path)
    add_tree_item(config.tree)


def add_tree_item(tree):
    x=tree.get_children()
    for item in x:
        tree.delete(item)
    root = tree.insert("",0,text=config.tree_data.name,values=(main_path,config.tree_data.isLeaf), open=True, image=folder_img)    
    add_sub_tree_item(tree, root, config.tree_data.children)


def add_sub_tree_item(tree, pid, children):
    for item in children:
        m_type = get_config(os.path.join(item.path, 'config.txt'), 'type')
        id = tree.insert(pid,'end',text=item.name,values=(item.path, item.isLeaf), image=folder_img if m_type=="dir" else file_img)
        add_sub_tree_item(tree, id, item.children)


def treeDbClick(event):
    for item in config.tree.selection():
        val = config.tree.item(item, "values")
        if val[1] == 'True':
            ConfigForm(val[0])


def bDown(event):
    global from_dir
    global from_iid
    tv = event.widget
    iid = tv.identify_row(event.y)
    val = config.tree.item(iid, "values")
    
    from_dir = val[0]
    from_iid = iid
    


def bUp(event):
    global from_dir
    global from_iid
    tv = event.widget
    iid = tv.identify_row(event.y)
    if not iid:
        return
    
    if iid == from_iid:
        return

    val = config.tree.item(iid, "values")
    m_type = get_config(os.path.join(val[0], 'config.txt'), 'type')

    if m_type != 'dir':
        return

    d = tk.simpledialog.SimpleDialog(window,
                    text="确认移动",
                    buttons=["Yes", "No"],
                    cancel=1,
                    title="移动")
    if d.go() == 0:
        move_dir(from_dir, val[0])


def move_dir(from_dir, to_dir):
    print("%s -> %s" % (from_dir, to_dir))
    if to_dir.startswith(from_dir):
        print('can\'t move dir to it\'s child')
        return

    os.rename(from_dir, os.path.join(to_dir, os.path.basename(from_dir)))
    refresh(None)


def get_config(config_file, key):
    with open(config_file, 'r', encoding='utf-8') as f:
        for i in f:
            s = i.split('=')
            if s[0].strip() == key:
                return s[1].strip()

    return None


class ConfigForm(tk.Toplevel):
    __path = None
    def __init__(self, path):
        super().__init__(master = window)
        self.__path = path
        self.init_widgets()

   
    def init_widgets(self):
        # 设置窗口大小
        winWidth = 600
        winHeight = 600
        # 获取屏幕分辨率
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        
        # 设置主窗口标题
        self.title("config")
        # 设置窗口初始位置在屏幕居中
        self.geometry("+%s+%s" % ( x, y))
        mainframe = ttk.Frame(self, padding='5 5')
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.S, tk.W))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        self.text = tkinter.scrolledtext.ScrolledText(mainframe, height=40)
        self.text.grid(column=0, row=0, columnspan= 3, sticky=(tk.N, tk.W))
        ttk.Button(mainframe, text='run', command =  self.btn_run_click).grid(column=3, row=1, sticky=tk.E)
        ttk.Button(mainframe, text='default', command =  self.btn_default_click).grid(column=2, row=1, sticky=tk.E)
        ttk.Button(mainframe, text='save as default', command =  self.btn_save_as_default_click).grid(column=1, row=1, sticky=tk.E)

        self.load_config()

    
    def load_config(self):
        if not os.path.exists(os.path.join(self.__path, 'user.py')):
            shutil.copy2(os.path.join(self.__path, "default.py"), os.path.join(self.__path, "user.py"))

        with open(os.path.join(self.__path, 'user.py'), "r", encoding="utf-8") as f:
            self.text.delete("1.0", tk.END)
            self.text.insert("1.0", f.read())      


    def btn_run_click(self):
        os.chdir(self.__path)
        with open(os.path.join(self.__path, "user.py"), "w", encoding = "utf-8") as f:
            f.write(self.text.get("1.0", tk.END))

        with open(os.path.join(self.__path, "input.txt"), "w", encoding = "utf-8") as f:
            f.write(config.input.get("1.0", tk.END))

        self.destroy()
        if threading.active_count() <= 1:
            config.t = threading.Thread(target=run_command, args=[os.path.join(self.__path, 'main.py')])
            config.t.start()
        else:
            tk.messagebox.showwarning("警告","同时只能一个任务执行")
        # run_command(os.path.join(self.__path, 'main.py'))
        # config.output.delete("1.0", tk.END)
        # config.output.insert("1.0", out)
        

    def btn_default_click(self):
        os.remove(os.path.join(self.__path, "user.py"))
        self.load_config()  
        

    def btn_save_as_default_click(self):
        with open(os.path.join(self.__path, "default.py"), "w", encoding = "utf-8") as f:
            f.write(self.text.get("1.0", tk.END))


class RightClick:
    def __init__(self, master):
        # create a popup menu
        self.aMenu = tk.Menu(master, tearoff=0)
        self.aMenu.add_command(label='运行', command=self.run)
        self.aMenu.add_command(label='打开文件夹', command=self.open_dir)
        self.aMenu.add_command(label='重命名...', command=self.rename)
        self.bMenu = tk.Menu(master, tearoff=0)
        self.bMenu.add_command(label='新建文件夹...', command=self.new_dir)
        self.bMenu.add_command(label='新建模块...', command=self.new_module)
        self.bMenu.add_command(label='重命名...', command=self.rename)
        self.tree_item = ''


    def run(self):
        if self.tree_item:
            val = config.tree.item(self.tree_item, "values")
            os.chdir(val[0])

            if not os.path.exists(os.path.join(val[0], 'user.py')):
                shutil.copy2(os.path.join(val[0], "default.py"), os.path.join(val[0], "user.py"))

            with open(os.path.join(val[0], "input.txt"), "w", encoding = "utf-8") as f:
                f.write(config.input.get("1.0", tk.END))

            print(threading.active_count() )
            if threading.active_count() <= 1:
                config.t = threading.Thread(target = run_command, args=[os.path.join(val[0], 'main.py')])
                config.t.start()
                
            else:
                tk.messagebox.showwarning("警告","同时只能一个任务执行")
            # run_command(os.path.join(val[0], 'main.py'))
            # config.output.delete("1.0", tk.END)
            # config.output.insert("1.0", out)


    def open_dir(self):
        if self.tree_item:
            val = config.tree.item(self.tree_item, "values")
            os.system("explorer %s" % val[0])

    
    def new_module(self):
        module_name = tkinter.simpledialog.askstring("新建模块", "请输入模块名称")
        if not module_name:
            return
        iid = config.tree.selection()[0]
        val = config.tree.item(iid, "values")
        path = os.path.join(val[0],'m_%04d' % common.get_seq_value("module"))
        os.mkdir(path)
        with open(os.path.join(path, "config.txt"), "w", encoding="utf-8") as f:
            f.write("name=%s\n" % module_name)
            f.write("type=module\n")

        with open(os.path.join(path, "main.py"), "w", encoding="utf-8") as f:
            f.write('import os\n')
            f.write('import sys\n')
            f.write('import user\n')
            f.write('\n')
            f.write('config = user.config()\n')
            f.write('\n')
            f.write('def main():\n')
            f.write('    print("hello world")\n')
            f.write('\n')
            f.write('if __name__ == "__main__":\n')
            f.write('    main()    \n')

        with open(os.path.join(path, "default.py"), "w", encoding="utf-8") as f:
            f.write('_config = {\n')    
            f.write('}\n')    
            f.write('\n')    
            f.write('def config():\n')    
            f.write('    return _config\n')
        refresh(None)


    def new_dir(self):
        dir_name = tkinter.simpledialog.askstring("新建文件夹", "请输入文件夹名称")
        if not dir_name:
            return
        iid = config.tree.selection()[0]
        val = config.tree.item(iid, "values")
        path = os.path.join(val[0],'d_%04d' % common.get_seq_value("dir"))
        os.mkdir(path)
        with open(os.path.join(path, "config.txt"), "w", encoding="utf-8") as f:
            f.write("name=%s\n" % dir_name)
            f.write("type=dir\n")
        refresh(None)


    def popup(self, event):
        iid = config.tree.identify_row(event.y)
        print("iid", iid)
        if iid:
            config.tree.selection_set(iid)
            val = config.tree.item(iid, "values")
            print("val", val)
            if val[1] == 'True':
                self.tree_item = iid
                self.aMenu.post(event.x_root, event.y_root)
            else:
                self.tree_item = iid
                self.bMenu.post(event.x_root, event.y_root)


    def rename(self):
        new_name = tkinter.simpledialog.askstring("重命名", "请输入新名称") 
        if new_name:
            iid = config.tree.selection()[0]
            val = config.tree.item(iid, "values")
            config_file = os.path.join(val[0],"config.txt")
            params = {}
            with open(config_file, "r", encoding="utf-8") as f:
                for l in f:
                    s = l.split("=")
                    params[s[0].strip()] = s[1].strip()
            with open(config_file, "w", encoding="utf-8") as f:
                for x in params:
                    if x == 'name':
                        f.write("name=%s\n"%new_name)
                    else:
                        f.write("%s=%s"%(x, params[x]))
            refresh(None)


                

if __name__ == '__main__':
    
    sys.exit(main())