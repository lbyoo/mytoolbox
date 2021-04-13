import os
import sys
import user

config = user.config()

def run(path):
    if os.path.isfile(path):
        if path.endswith(config['suffix']):
            with open(path, "r", encoding="utf-8") as f:
                tmpfile = open(path+'.tmp', 'w+b')
                for line in f:
                    line = line.replace('\r', '')
                    line = line.replace('\n', '')
                    tmpfile.write((line+'\n').encode("utf-8"))
                tmpfile.close()
            os.remove(path)
            os.rename(path+'.tmp', path)
    
    if os.path.isdir(path):
        for f in os.listdir(path):
            run(os.path.join(path,f))

def main():
    run(config["path"])

if __name__ == "__main__":
    main()    
