import threading
import socket
import pgpy
from random import randint


def datagram():
    sh = randint(a=0, b=10)
    ori = bool(randint(a=0, b=1))

    header = {
        "orientation": ori,
        "shuffle": sh,
        "ciphertext": "4spk63eAxsnI/B5ErUNSCJwN+9X0Eclmqck/zy3o7Iu/aRxPyxUytjUrI0rD2e4="
    }


def connect(conn):
    while True:
        received = conn.recv(1024)
        if received == ' ':
            pass
        else:
            print('\n' + received.decode())


def sendMsg(conn):
    while True:
        send_msg = input().replace('b', '').encode()
        if send_msg == ' ':
            pass
        else:
            conn.sendall(send_msg)


def encapsulate(s):
    pass


def handshake(s):
    # gera criptografia
    key = pgpy.PGPKey.new(pgpy.PubKeyAlgorithm.RSAEncryptOrSign, 1024)
    key = encapsulate(key)
    s.sendall(key)
    publickey = s.recv(1024)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 800))
    s.listen()
    (conn, addr) = s.accept()
    handshake(s)
    thread1 = threading.Thread(target=connect, args=([conn]))
    thread2 = threading.Thread(target=sendMsg, args=([conn]))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()