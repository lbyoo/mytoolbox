#coding:utf-8
import re

with open("../input.txt","r") as f:
    for line in f.readlines():
        if re.match( r"^(?P<va>.*\.[hc]) .*", line) != None:
            s = line.split()
            print(f"{s[0]:50}  {s[3]}")



