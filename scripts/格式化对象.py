#coding:utf-8
import json

with open("d:/python_project/my_toolbox/input.txt","r", encoding="utf8") as f:
    data = f.read().replace(" ","")

level = 0
indent = 2

pre = None
startQuote = 0
for c in data:
    if c in  ["(", "{", "["]:
        print(c, end = "")
        level += 1
        print()
        print(" " * level * indent, end = "")
    elif c == ",":
        print(c, end = "")
        if startQuote == 0:
            print()
            print(" " * level * indent, end = "")
    elif c in [")", "}", "]"]:
        print()
        level -= 1
        print(" " * level * indent, end = "")
        print(c, end = "")
    elif c in ["\"", "\'"]:
        print(c, end = "")
        startQuote = 1 - startQuote
    else:
        print(c, end = "")

print()



