import os
import sys
import user

config = user.config()

os.chdir("D:\\python_project\\my_toolbox\\tea_main\\generated-code")
os.mkdir(config["path"])

with open(os.path.join(config["path"], "config.txt"), "w", encoding="utf-8") as f:
    f.write("name=%s\n"%config["name"])
    f.write("type=module\n")

with open(os.path.join(config["path"], "default.py"), "w", encoding="utf-8") as f:
    f.write(config["template-default"])

with open(os.path.join(config["path"], "main.py"), "w", encoding="utf-8") as f:
    f.write(config["template-main"])

print("generate code ok")
# print("code path：[%s%s]" % ("D:/python_project/my_toolbox/tea_main/generated-code/", config["path"]))