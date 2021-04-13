import os
import sys
import user
from urllib import parse

config = user.config()
with open("input.txt", "r", encoding="utf-8") as f:
    input_text = f.read().strip("\n")



def main():
    print(parse.quote_plus(input_text))
    print(parse.quote(input_text))


if __name__ == "__main__":
    main()    
