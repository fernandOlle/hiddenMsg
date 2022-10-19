import threading
import socket
import rsa
from random import randint
from datagram_utils import *

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 9090))
    s.listen()
    (conn, addr) = s.accept()
    thread1 = threading.Thread(target=receive, args=([conn]))
    thread2 = threading.Thread(target=send, args=([conn]))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
