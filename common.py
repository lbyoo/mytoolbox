import os
import sys
import threading
import time
import ctypes
import inspect
import asyncio

class Dict(dict):
    """
    字典对象
    实现一个简单的可以通过属性访问的字典，比如 x.key = value
    """
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def to_class_name(s):
    return "".join([x.capitalize() for x in s.split("_")])


def to_field_name(s):
    s = "".join([x.capitalize() for x in s.split("_")])
    return s[0:1].lower() + s[1:]


def get_seq_value(seq_name):
    path = os.path.dirname(sys.argv[0])
    with open(os.path.join(path, 'config.txt'), 'r', encoding='utf-8') as f:
        c = eval(f.read())
    if seq_name in c:
        val = c[seq_name]
    else:
        val = 0
    c[seq_name] = val + 1
    with open(os.path.join(path, 'config.txt'), 'w', encoding='utf-8') as f:
        f.write(str(c))
    return val    


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    try:
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            # pass
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    except Exception as err:
        print(err)


def stop_thread(thread):
    """终止线程"""
    _async_raise(thread.ident, SystemExit)    