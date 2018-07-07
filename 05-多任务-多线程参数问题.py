# python解释器中有一个模块,专门用于操作线程
import threading
import time


# 发送消息
def send_msg(num):
    # print(threading.current_thread())
    for i in range(num):
        print('发送...', i+1)
        time.sleep(0.1)


# 接收消息
def receive_msg(name, age, address):
    # print(threading.current_thread())
    time.sleep(0.05)
    print(name, age, address)


# 程序入口
if __name__ == '__main__':
    # 可以利用threading模块里面的Thread创建线程对象
    #       注意: 传递函数作为参数的时候,函数后面不能带括号
    #   t1是子线程1  都是主线程创建的
    t1 = threading.Thread(group=None, target=send_msg, name='send', args=(3,))
    #   t2是子线程2  都是主线程创建的
    t1.start()
    t1.join()
    t2 = threading.Thread(group=None, target=receive_msg, name='recv', kwargs={'name': '张三', 'age': 18, 'address': '三里屯'})
    t2.start()
    t2.join()
