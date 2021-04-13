# coding:utf-8

from urllib import request, parse

with open("D:/python_project/my_toolbox/input.txt", "r", encoding="utf-8") as f:
    txt = f.read().strip()
    print(txt)
    print("----------------------------------------")

print(parse.quote(txt))