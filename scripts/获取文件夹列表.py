#coding:utf-8
import os
import sys
import codecs
import chinese_encode
# reload(sys)
# sys.setdefaultencoding('utf-8')
#全局配置信息
path = "d:/"
dir_only = True

#主程序开始
def main():
    with open("../output/data.txt", "w") as f:
        for line in os.listdir(path):
            abspath = os.path.join(path,line)
            if not dir_only:
                f.write(abspath + "\n")

            elif os.path.isdir(abspath):
                f.write(abspath + "\n")


    # print [ chinese_encode.GetStrFromUnicode(os.path.abspath(x)) for x in  ]


if __name__ == '__main__':
    main()