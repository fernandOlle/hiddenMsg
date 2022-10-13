import sys
import socket
import threading
from datagram_utils import *


header = {
    "orientation": ori,
    "shuffle": sh,
    "ciphertext": "4spk63eAxsnI/B5ErUNSCJwN+9X0Eclmqck/zy3o7Iu/aRxPyxUytjUrI0rD2e4="
}


def connect(s):
    while True:
        r_msg = s.recv(1024)
        if not r_msg:
            break
        if r_msg == '':
            pass
        elif sys.sdtin().len() < 0:
            print('\n' + r_msg.decode())


def receive(s):
    while True:
        s_msg = input().replace('b', '').encode('utf-8')
        if s_msg == '':
            pass
        if s_msg.decode() == 'exit':
            print("wan exit")
            break
        else:
            s.sendall(s_msg)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: %s [ip adress][port] " % sys.argv[0])
        sys.exit(0)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((sys.argv[1], int(sys.argv[2])))
    handshake(s)
    thread1 = threading.Thread(target=connect, args=([s]))
    thread2 = threading.Thread(target=receive, args=([s]))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
