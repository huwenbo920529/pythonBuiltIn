# coding:utf-8
from socket import *
import time


s = socket(AF_INET, SOCK_STREAM)  # 创建TCP套接字
s.bind(('', 8888))  # 绑定到端口8888
s.listen(5)  # 监听，但只能挂起5个以下的连接
while True:
    client, addr = s.accept()
    print "Got a connection from {}".format(str(addr))
    timestr = time.ctime(time.time()) + "\r\n"
    client.send(timestr.encode('ascii'))
    client.close()

