import os
import sys
import user

config = user.config()

root = config['img_dir']
# root = r"D:\iot\切图1"
# outfile = "../output/list.html"
outfile = root + r"\list.html"
# temp = '''<div class="panel"><div class="ico"><embed src="{0}" width="100" type="image/svg+xml" pluginspage="http://www.adobe.com/svg/viewer/install/" /></div><div class="label"><p>{1}</p></div></div>'''
temppic = '''<div class="panel"><div class="ico"><img src="{0}" width="100" /></div><div class="label"><p>{1}</p></div></div>'''

style = '''<style>
.panel{
    margin-left: 15px;
    margin-top: 15px;
    background-color: #ddd;
    width:200px;
    height:200px;
    float:left;
    box-shadow: -10px -10px 15px rgba(255,255,255,0.7), 10px 10px 15px rgba(70,70,70,0.3),inset -10px -10px 15px rgba(255,255,255,0.5), inset 10px 10px 15px rgba(70,70,70,0.12);
    border-radius:15px;

}
.label{
    display: flex;
    align-items: center;
    justify-content: center;
    height:60px;
    margin-top:10px;


}

.ico{
    margin: auto;
    width:100%;
    height:130px;
    display: flex;
    align-items: center;
    justify-content: center;


}
.bar{
    background-color:#fff;
    margin:1px;
    padding:3px;
    box-shadow: 2px 2px 15px rgba(128,128,128,0.3)

}
.content{
    float:left;
    width:100%;

    margin-top:20px;
}
body {
    background-color:#eef;
}
</style>'''

def fprint(s):
    f.write(s + "\n")


def work_file(path, file):
    fprint(temppic.format(path + "/" + file, file))


def work(path,fullpath = "."):
    ext = [".svg", ".jpg", ".png", ".jpeg"]
    os.chdir(path)
    files = os.listdir()
    hasfile = False
    #print(files)
    for file in files :
        if os.path.isdir(file):
            work(file, fullpath + "/" + file)
        else:
            t = os.path.splitext(file)[1]
            if t in ext:
                if not hasfile:
                    fprint( f"<div class=\"content\"><div class=\"bar\"> {fullpath}</div>")
                    hasfile = True
                work_file(fullpath, file)
    if hasfile:
        fprint( "</div>")

    os.chdir("..")
    # fprint("</div>")


def main():
    global f
    f = open(outfile, "w")
    os.chdir(root)
    fprint("<html>")
    fprint(style)
    fprint("<body>")
    work(root)
    fprint("</body></html>")
    f.close()
    print("chrome.exe %s" % outfile)
    os.system("\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" %s" % outfile)
    

if __name__ == "__main__":
    main()    
