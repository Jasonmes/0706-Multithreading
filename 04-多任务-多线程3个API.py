# python解释器中有一个模块,专门用于操作线程
# import threading
# import time
# # 发送消息
# def send_msg():
#     # 线程1
#     print(threading.current_thread(), type(threading.current_thread()))
#     for i in range(5):
#         print('发送...', i+1)
#         time.sleep(0.1)
# # 接收消息
# def receive_msg():
#     # 线程2
#     print(threading.current_thread(), type(threading.current_thread()))
#     for i in range(5):
#         print('接收消息...', i+1)
#         time.sleep(0.1)
# # 程序入口
# if __name__ == '__main__':
#     # 1.线程列表;(必须启动后才有)
#     # print(threading.enumerate())
#     # 2.当前线程
#     # print(threading.current_thread(), type(threading.current_thread()))
#     #
#     # # 3.活动线程数量;  线程列表的长度
#     #
#     # # 可以利用threading模块里面的Thread创建线程对象
#     t1 = threading.Thread(target=send_msg)
#     t2 = threading.Thread(target=receive_msg)
#     print("活动线程数量", threading.active_count())
#     # # print(threading.enumerate())
#     #
#     # # 开启线程
#     t1.start()
#     t2.start()
#     #
#     # # 开启以后,就会进入线程列表
#     print(threading.enumerate())
#     #
#     # print("活动线程数量", threading.active_count())

import threading
import time


if __name__ == '__main__':
    thread1 = threading.Thread(target=send_data)
    thread2 = threading.Thread(target=get_data)
    thread1.start()
    thread2.start()
    print(threading.current_thread())
    print(threading.enumerate())
    print(threading.active_count())