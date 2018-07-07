# python解释器中有一个模块,专门用于操作线程
# import threading
# import time
#
#
# # 发送消息
# def send_msg():
#     for i in range(5):
#         print('发送...', i+1)
#         time.sleep(0.1)
#
#
# # 接受消息
# def receive_msg(name, age, address):
#     # print(threading.current_thread())
#     time.sleep(0.05)
#     print(name, age, address)
#
#
# # 程序入口
# if __name__ == '__main__':
#     # 可以利用threading模块里面的Thread创建线程对象
#     #       注意: 传递函数作为参数的时候,函数后面不能带括号
#     #   t1是子线程1  都是主线程创建的
#     t1 = threading.Thread(group=None, target=send_msg, name='send', args=(3,))
#     #   t2是子线程2  都是主线程创建的
#
#     t2 = threading.Thread(group=None, target=receive_msg, name='recv',
#                           kwargs={'name': '张三', 'age': 18, 'address': '三里屯'})
#
#     # 3.守护线程,必须在子线程开启之前设置;(要设置守护线程,一般就都设置)
#     t1.setDaemon(True)
#     t2.setDaemon(True)
#
#     # 开启线程
#     t1.start()
#     t1.join()
#     t2.start()
#     t2.join()
#     # 2.线程等待
#     # 1.主线程和子线程默认的执行顺序: 主线程优先执代码行完毕,然后在文件的最末尾等待子线程执行完毕,在退出程序;
#     #   2.需求(线程等待): 子线程走完了,主线程在走;(主线程暂停等待子线程)
#     #   3.需求(守护线程): 主线程走完了,子线程立即停止;
#     print('主线程执代码行完毕!!!!!!!')

# 第一遍
# 假如说A线程里面创建了子线程B，A使用了setDaemon()，
# B使用了join()，因为join会阻塞A线程直到B结束之后，才会到A执行
# import threading
# import time
#
#
# def test():
#     a, b, c = range(3)
#     lu = [[a, '小狗'],
#           [b],
#           [[c, 3], '小龙']]
#     print(lu[c][b])
#
#
# def get_data(num):
#     for i in range(num):
#         print('run..', i + 1)
#         time.sleep(0.02)
#     _3thread = threading.Thread(target=test)
#     _3thread.start()
#     _3thread.join()
#
#
# def send_data(name, age, youku):
#     print(name, age, youku)
#
#
# if __name__ == '__main__':
#     _1thread = threading.Thread(group=None, target=get_data, args=(3,))
#     _1thread.setDaemon(True)
#
#     _2thread = threading.Thread(group=None, target=send_data, kwargs={'name': 'jason', 'age': 18, 'youku': 90})
#
#     _1thread.start()
#     _1thread.join()
#
#     _2thread.start()
#     _2thread.join()

# 第二遍
# import threading
# import time
#
#
# def _algorithm():
#     a, b, c = range(3)
#     algori = [[a, 'Yes'],
#             [b],
#             [[c, 'Dog'], a]]
#     print(algori[c][a][b])
#
#
# def _3thread(num):
#     for i in range(num):
#         print('run', i + 1)
#         time.sleep(0.02)
#
#     _3 = threading.Thread(target=_algorithm)
#     _3.start()
#     _3.join()
#
#
# def _kwargs(name, age, youku):
#     print(name, age, youku)
#
#
# if __name__ == '__main__':
#     _2threading = threading.Thread(group=None, target=_3thread, args=(4,))
#     _2threading.setDaemon(True)
#     _2threading.start()
#     _2threading.join()
#
#     _3threading = threading.Thread(group=None, target=_kwargs, kwargs={'name': 'wotson', 'age': 18, 'youku': 90})
#     _3threading.start()

# 第三遍
import threading
import time


def _alogorithm():
    a, b, c = range(3)
    tree = [[a, 'who'],
            [b],
            [[c, 'run'], c]]
    print(tree[c][a][b])


def _3thread(num):
    for i in range(num):
        print('run', i + 1)
        time.sleep(0.05)
    _Algorithm = threading.Thread(target=_alogorithm)
    _Algorithm.start()
    _Algorithm.join()


def _kwargs(name, age, youku):
    print(name, age, youku)


if __name__ == '__main__':
    _3thre = threading.Thread(group=None, target=_3thread, args=(4,))
    _3thre.setDaemon(True)
    _3thre.start()
    _3thre.join()

    _4thre = threading.Thread(group=None, target=_kwargs, kwargs={'name': 'is me', 'age': 28, 'youku': 'http://www.youku.com'})
    _4thre.start()