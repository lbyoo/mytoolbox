#!/usr/bin/env python3
import os
import sys
import re

file = "D:/v2x/广汽QAC修改/GAC-REPORT-EACH-FILE/TC-report.txt"
filtes = ("7", )

def del_lines(lines, i):
    st = i
    j = i + 2
    while True:
        if lines[j].startswith("Msg("):
            del lines[i: i + 2]
            break
        elif lines[j].startswith("-->("):
            del lines[j]
            continue
        else:
            if lines[i - 1].strip() == "^":
                del lines[i - 1: i + 2]
                st = i - 1
            else:
                del lines[i: i + 2]
                
            
            break
    
    return st


with open(file, "r", encoding="utf8") as fr:
    lines = fr.readlines()
    
i = 0

while i < len(lines):
    if lines[i].startswith("Msg("):
        if lines[i][4] in filtes:
            i += 1

        else:
            st = del_lines(lines, i)
            
            i -= 1 + (i - st)

    i += 1

with open(file + ".txt", "w", encoding="utf8") as fw:
    fw.writelines(lines)

    