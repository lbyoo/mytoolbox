_config = {
    
    "name": "生成java set代码",
    "path": "gen_java_set",
    "template-main": '''
import os
import sys
import user

config = user.config()

def main():
    print("hello world1")

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








