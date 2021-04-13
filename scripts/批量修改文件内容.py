#coding:utf-8

import os
import sys

path = "d:/test"

ext = [".c", ".h", ".H", ".C"]
kv = {"ngx": "lby", "NGX": "LBY"}

def work_file(temp):

    with open(temp, "r") as fr:
        content = fr.read()
    for k in kv:
        content = content.replace(k, kv[k])
    with open(f"{temp}.tmp", "w") as fw:
        fw.write(content)
    os.remove(temp)
    os.rename(f"{temp}.tmp", temp)


def work(path):
    print(f"cd {path}")
    os.chdir(path)
    files = os.listdir()
    #print(files)
    for file in files :
        if os.path.isdir(file):
            work(file)
        else:
            t = os.path.splitext(file)[1]
            if t in ext:
                work_file(file)

    os.chdir("..")

work(path)