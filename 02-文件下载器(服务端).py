# 1.接受客户端的链接请求,然后接收一个文件名
import socket


# 我在尝试上传文件的时候，第一步暂时只是把txt内容上传到服务端，一开始我不理解，我本意是把整个文件都上传，结果博哥告诉我，其实本质就是读取文件本身二进制，
# 然后传输给服务器，服务器再进行转换得到文件。
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
tcp_socket.bind(('', 9891))
tcp_socket.listen(128)
while True:
    service_client_socket, ip_port = tcp_socket.accept()
    # file_name = service_client_socket.recv(1024).decode(encoding='utf-8')
    file_content = service_client_socket.recv(1024).decode(encoding='utf-8')
    with open('./download/' + '123.txt', 'w') as file:
        while True:
            if file_content:
                file.write(file_content)
                print('文件写入成功')
                break
            else:
                print('文件不存在,或者读取异常...')
                break
    service_client_socket.close()
tcp_socket.close()
