import sys
import socket
import threading
import rsa
from datagram_utils import *

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("uso: %s [ip adress] [port] " % sys.argv[0])
        sys.exit(0)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((sys.argv[1], int(sys.argv[2])))
    thread1 = threading.Thread(target=receive, args=([s]))
    thread2 = threading.Thread(target=send, args=([s]))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
