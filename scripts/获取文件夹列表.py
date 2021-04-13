#coding:utf-8
import os
import sys
import codecs
import chinese_encode
# reload(sys)
# sys.setdefaultencoding('utf-8')
#全局配置信息
path = "D:\\v2x\\branch\\1609_facility_r4.0_feature"
ignore = [".git", ".vscode"]
filter_str = "MSA"
dir_only = False


def search_path(path, f):
    for file in os.listdir(path):
        if file in ignore:
            continue
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            f.write(filepath + "\n")
            search_path(filepath,f)
        elif os.path.isfile(filepath) and not dir_only:
            if filepath.find(filter_str) >= 0:
                f.write(filepath + "\n")


#主程序开始
def main():
    with open("../output/data.txt", "w") as f:
        search_path(path, f)


if __name__ == '__main__':
    main()