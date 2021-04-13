import os
import sys
import user
from urllib import request, parse
from Crypto.Cipher import AES


#https忽略校验
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

config = user.config()
url = config["m3u8-index"]
dest_str = parse.urlparse(url)


def main():
    if not os.path.exists("out"):
        os.mkdir("out")

    resp = urlopen(url)
    for i in resp.decode("utf-8").split("\n"):
        if i and not i.startswith("#EXT"):
            craw(dest_str.scheme + "://" + dest_str.netloc + i)


def urlopen(url):
    print("open:", url)
    req = request.Request(url)
    req.add_header('User-Agent', config["user-agent"])
    f = request.urlopen(req)
    return f.read()

def craw(url):
    global cipher
    resp = urlopen(url)
    # print(resp[:300])
    lines = resp.decode("utf-8").split("\n")
    total = len([x for x in lines if not x.startswith("#EXT") and x])
    current = 0
    for i in lines:
        if i.startswith("#EXT-X-KEY"):
            key = parse_key(i)
            cipher = AES.new(key, AES.MODE_CBC, key)
        
        if i and not i.startswith("#EXT"):
            current += 1
            craw_ts(i, "%d/%d" %(current, total))

    f = open("out/final.mp4", "w+b")
    for i in lines:
        if i and not i.startswith("#EXT"):
            merge(f, i)
    f.close()


def merge(f, url):
    filename = url.split("/")[-1]
    with open("out/%s"%filename, "rb") as fr:
        f.write(fr.read())


def parse_key(s):
    url = s[s.index('URI=') + 5:-1]
    resp = urlopen(url)
    return resp
    
                
    
def craw_ts(url, desc):
    filename = url.split("/")[-1]
    if os.path.exists("out/%s"%filename):
        print(filename, "skip", desc)
        return

    print("download:", filename, desc)
    resp = urlopen(url)
    data = cipher.decrypt(resp)
    with open("out/%s"%filename, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    main()    
