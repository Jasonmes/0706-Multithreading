# 有的时候,如果代码量太大了,需要自定义线程类,实现多线程,多任务...
import threading
import time


# # 如果我们向自定义线程类,那么就要继承线程类
# class Send(threading.Thread):
#     # 定义__init__()接收参数
#     def __init__(self, num):
#         # 继承的时候
#         # 如果重写__init__(),还要保证父类中的逻辑正常执行
#         super().__init__()
#         self.num = num
#
#     # 发送消息
#     def send(self):
#         for i in range(self.num):
#             print('发送....', i+1)
#             time.sleep(0.1)
#
#     # 如果想要让send被多线程执行,那么就要把send方法写入run方法中...
#     def run(self):
#         self.send()
#
#
# # 如果我们向自定义线程类,那么就要继承线程类
# class Receive(threading.Thread):
#     # 接收消息
#     def receive(self):
#         for i in range(5):
#             print('接收消息....', i+1)
#             time.sleep(0.1)
#
#     # 如果想要让send被多线程执行,那么就要把send方法写入run方法中...
#     def run(self):
#         self.receive()
#
#
# if __name__ == '__main__':
#     # 创建两个自定义类的对象
#     t1 = Send(3)
#     t2 = Receive()
#
#     # 开启线程
#     t1.start()
#     # start(): 底层应该是默认调用run()
#     t2.start()

# 第一遍
# class _send(threading.Thread):
#     def __init__(self, num):
#         super().__init__()
#         self.num = num
#
#     def send(self):
#         for i in range(self.num):
#             print("run", i + 1)
#             time.sleep(0.03)
#
#     def run(self):
#         self.send()
#
#
# class receive(threading.Thread):
#     def rec(self):
#         for i in range(3):
#             print('go', i + 1)
#             time.sleep(0.02)
#
#     def run(self):
#         self.rec()
#
#
# if __name__ == '__main__':
#     s = _send(3)
#     r = receive()
#
#     s.start()
#     r.start()

# 第二遍
# class _run(threading.Thread):
#     def __init__(self, num):
#         super().__init__()
#         self.num = num
#
#     def print_2(self):
#         for i in range(self.num):
#             print('run', i + 1)
#             time.sleep(0.04)
#
#     def run(self):
#         self.print_2()
#
#
# class _go(threading.Thread):
#     def go(self):
#         for i in range(3):
#             print('go', i + 1)
#
#     def run(self):
#         self.go()
#
#
# if __name__ == '__main__':
#     ru = _run(3)
#     go = _go()
#     ru.start()
#     ru.join()
#     go.start()