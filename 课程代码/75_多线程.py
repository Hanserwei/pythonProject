import threading
import time
from threading import Thread


def sing():
    while True:
        print("我是傻逼！")
        time.sleep(1)

def dance():
    while True:
        print("你是傻逼！")
        time.sleep(1)

if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()