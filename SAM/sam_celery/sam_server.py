# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/7 11:16'
# file : 'sam_server.py'
# Summary : ''


import socket
import threading
import time


def tcplink(sock, addr):
    print('accept new connection for %s: %s...' % addr)
    sock.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s: %s closed.' % addr)


def main():
    s = socket.socket()
    s.bind(('192.168.1.141', 8080))
    s.listen(5)
    print('waiting for connection ...')
    while True:
        # 接收一个新连接
        sock, addr = s.accept()
        print(f'sock: {sock}, addr: {addr}')
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


if __name__ == '__main__':
    main()
