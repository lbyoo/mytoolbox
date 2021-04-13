#coding:utf-8
import re

#全局配置信息
input_file = "../input.txt"
output_file = "../output/data.txt"

#匹配保留字符串的正则表达式
prog = re.compile(".*\.h")

#主程序开始
def main():
    with open(input_file,"r") as f:
        if output_file:
            with open(output_file,"w") as fo:
                for line in f:
                    work(line,fo)
        else:
            work(line)

def work(line,fo = None):
    s = line.strip("\n")
    result = prog.match(s)
    if result != None:
        fo.write("{}\n".format(s))
        print(s)


if __name__ == '__main__':
    main()