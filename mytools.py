#!/usr/bin/env python3
#coding:utf-8

import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))
script_path = "scripts"

cmds = {}
files = [x for x in os.listdir(script_path) if x.endswith(".py")]
for n, file in enumerate(files):
    print("{}: {}".format(n, file))
    cmds[str(n)] = file
n = input("please input number:")
print("{}/{}".format(script_path, cmds[n]))
os.system("python3 {}/{}".format(script_path, cmds[n]))


