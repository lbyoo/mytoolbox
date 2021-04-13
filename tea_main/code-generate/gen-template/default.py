_config = {
    
    "name": "小工具",
    "path": "mydir",
    "template-main": '''
import os
import sys
import user

config = user.config()

def main():
    print("hello world")

if __name__ == "__main__":
    main()    

''',
"template-default": '''
_config = {

    
    
    }


def config():
    return _config       
    '''
    
    
    
    
    
    }



def config():
    return _config