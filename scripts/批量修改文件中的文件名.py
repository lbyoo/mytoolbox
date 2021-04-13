# coding:utf-8
import os
import sys

path = "d:/test"

s1 = ".txt"
s2 = ".c"

def work(path):
    print(f"cd {path}")
    os.chdir(path)
    files = os.listdir()
    #print(files)
    for file in files :
        if os.path.isdir(file):
            work(file)
        else:
            temp = file.replace(s1,s2)
            if temp != file:
                print(f"{file} -> {temp}")
                os.rename(file, temp)
    os.chdir("..")

work(path)        
