# 1.如果数据量太大,那么我们建议使用tcp发送信息的时候循环发送;
#     对方就要循环接收!   什么时候接收停止呢?  对方不发送为止,或者关闭链接...(b'')

# 2.如果是服务端,我们会使用死循环接收客户端发送的链接请求;
#     以后多任务的时候就可以同一时间多个客户端链接服务端了...
# while True:
    # tcp_socket.accept();

# 3.服务端使用socket出问题后,停止程序在开启该端口会有2-5分钟的禁止使用;
import socket
# tcp_socet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 无论tcp还是udp的socket都可以直接设置端口复用
#   setsockopt: 设置socket功能选项
#   socket.SOL_SOCKET: 当前socket
#   socket.SO_REUSEADDR: 复用端口
#   True/1: 同意复用
# (设置端口之前,设置他  bind...)
# tcp_socet.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# first time
# we use the dead loop to accept client's link requests send
# while True:
    # tcp_socet.accept()

# second time
# we use the dead loop to accept the client's link requests send
# while True:
#     tcp_socet.accept()

# third time
# use the dead loop tu accept the client's link requests send
# while True:
#     tcp_socet.accept()

# socket.SOL_SOCKET: current socket
# socket.SO_REUSEADDR : reuse Port,
# 1 is True
# _1timetcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# _1timetcps.setsockopt(socket.AF_INET, socket.SO_REUSEADDR, 1)


# _2timetcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# _2timetcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# _3timeTcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# _3timeTcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
