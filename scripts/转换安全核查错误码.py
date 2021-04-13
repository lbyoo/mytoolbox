#coding:utf-8
import re

with open("../input.txt","r", encoding="utf8") as f:
    data = f.read().replace(" ","").replace("/","").replace("*","").split("\n")

for n, item in enumerate(data):
    print("securityCodeMap.put(\"{}\", \"{}\");".format(n, re.sub(r'\d','',item.split(",")[1])))
