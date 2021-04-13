
import os
import sys
import user
import re
from io import StringIO

m = re.compile('.*\\sclass\\s+(\\S+)\\s')
m1 = re.compile(".*(set\\w+?)\\(.*")
config = user.config()


def main():
    class_name = config["class"]
    with open("input.txt","r", encoding="utf-8") as s:
        f = []
        while True:
            l = s.readline()
            if not l:
                break

            
            b = m1.match(l)
            if b:
                f.append(b[1])
        for x in f:        
            print("{}.{}();".format(class_name,x))
        
   


if __name__ == "__main__":
    main()    

