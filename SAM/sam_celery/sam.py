# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/7 10:18'
# file : 'sam.py'
# Summary : ''


import socket


def main():
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket()  # 使用默认值，跟上面一样
    s.connect(('192.168.1.141', 8080))
    print(s.recv(1024).decode('utf-8'))
    for data in [b'sam', b'turentu', b'admin']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()


if __name__ == '__main__':
    main()
