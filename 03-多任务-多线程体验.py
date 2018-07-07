# python解释器中有一个模块,专门用于操作线程
import threading
import time

#
# # 发送消息
# def send_msg():
#     for i in range(5):
#         print('发送...', i+1)
#         time.sleep(0.1)
#
#
# # 接收消息
# def receive_msg():
#     for i in range(5):
#         print('接收消息...', i+1)
#         time.sleep(0.1)
#
#
# # 程序入口
# if __name__ == '__main__':
#     # 可以利用threading模块里面的Thread创建线程对象
#     #       注意: 传递函数作为参数的时候,函数后面不能带括号
#     #   t1是子线程1  都是主线程创建的
#     t1 = threading.Thread(target=send_msg)
#     #   t2是子线程2  都是主线程创建的
#     t2 = threading.Thread(target=receive_msg)
#
#     # 开启线程
#     t1.start()
#      t2.start()

# first time
import threading
import time


def send_data():
    for i in range(5):
        print('i', i + 1)
        time.sleep(0.02)


def get_data():
    for i in range(5):
        print('i', i + 1)
        time.sleep(0.02)


if __name__ == '__main__':
    thread1 = threading.Thread(target=send_data)
    thread2 = threading.Thread(target=get_data)
    thread1.start()
    thread2.start()