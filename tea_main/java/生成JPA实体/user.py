import pymysql
_config = {
    "use_lombok": False,
    "table_name": "iot_device",
    "mysql": {
            'host':'vhost3',
            'port':3306,
            'user':'root',
            'password':'mysql',
            'db':'realsightiot',
            'charset':'utf8',
            'cursorclass':pymysql.cursors.DictCursor,
            }

}


def config():
    return _config





