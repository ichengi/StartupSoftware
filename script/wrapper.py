# -*-coding:utf-8-*-
'''
使用的装饰器
'''
import time


def wait_seconds(seconds:int):
    """等待指定秒数"""
    def wrapper(func):
        def inner(*args, **kwargs):
            time.sleep(seconds)
            ret = func(*args, **kwargs)

            return ret
        return inner
    return wrapper
