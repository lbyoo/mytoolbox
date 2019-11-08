#coding:utf-8

#全局配置信息
input_file = "../input.txt"
output_file = "../output/data.txt"

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
    s = line.strip("\n").split(" ")
    if fo:
        fo.write("%-25s%s\n" % (s[0]," ".join(s[1:])))

    print "%-25s%s" % (s[0]," ".join(s[1:]))


if __name__ == '__main__':
    main()