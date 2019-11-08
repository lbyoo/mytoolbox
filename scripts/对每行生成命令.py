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
    s = line.strip("\n")
    tmp = "ln -s /system/app/lib/{0} /opt/v2x/lib/{0}\n".format(s)
    if fo:
        fo.write(tmp)

    print(tmp)


if __name__ == '__main__':
    main()