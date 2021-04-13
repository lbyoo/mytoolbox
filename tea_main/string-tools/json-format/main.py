#coding:utf-8
import json
import user
config = user.config()
with open("input.txt","r", encoding="utf8") as f:
    data = f.read().replace(" ","").replace("\n", "")

level = 0
indent = config.get("indent") if "indent" in config else 2
# indent = 2

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



