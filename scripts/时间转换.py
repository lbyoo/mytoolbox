#!/usr/bin/env python3

import time
import datetime
print("当前时间:")
print(datetime.datetime.now())
print(time.time())
ts = 1592323200     #单位秒
with open("D:/python_project/my_toolbox/input.txt", "r") as f:
    ts = int(f.read())

dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
print("-------------------------------")
print("格式化时间:")
print(dt)
d = datetime.datetime.strptime("2020-06-17 00:00:00",'%Y-%m-%d %H:%M:%S')
print(int(d.timestamp()))

