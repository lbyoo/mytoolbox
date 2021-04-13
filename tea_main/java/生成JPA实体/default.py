import pymysql
_config = {
    "use_lombok": True,
    "table_name": "iot_template",
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

