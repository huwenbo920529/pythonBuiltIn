# coding: utf-8
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))  # 连接到服务器
tm = s.recv(1024)  # 最多接受1024个字节
s.close()
print "The time is {}".format(tm.decode('ascii'))
