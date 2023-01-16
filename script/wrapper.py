# -*-coding:utf-8-*-
'''
使用的装饰器
'''
import time
import pyautogui


def wait_seconds(seconds:int):
    """等待指定秒数"""
    def wrapper(func):
        def inner(*args, **kwargs):
            time.sleep(seconds)
            ret = func(*args, **kwargs)

            return ret
        return inner
    return wrapper

def is_open(img_path:str):
    """测试程序是否打开成功"""
    def wrapper(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            charge = pyautogui.locateOnScreen(img_path, confidence=0.75, grayscale=True)
            if charge is None:
                return False
            return ret
        return inner
    return wrapper

