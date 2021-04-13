#!/usr/bin/env python3

import time
import datetime
import os

ts = time.time() - 3600 * 8
# ts = 1592323200     #单位秒
     
     

host = input("Please input remote host(user@host):")
dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
print(dt)
print("ssh {} TZ='Asia/Shanghai' date -s '{}'".format(host, dt))
os.system("ssh {} \"TZ='UTC' date -s '{}'\"".format(host, dt))
