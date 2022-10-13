from rsa import *
from random import randint


pub_key = None
priv_key = None

their_pub_key = None

ori = None
sh = None

header = {
    "orientation": ori,
    "shuffle": sh,
    "ciphertext": "4spk63eAxsnI/B5ErUNSCJwN+9X0Eclmqck/zy3o7Iu/aRxPyxUytjUrI0rD2e4="
}


def desencapsulate(datagram: header):
    # desempacota a message
    sh = datagram["shuffle"]
    ori = datagram["orientation"]
    string = datagram["ciphertext"]

    if ori:
        new_string = None
        for char in string:
            new_string = ord(char)
            hodler += -sh
            new_string = chr(new_string)
        return new_string
    else:
        new_string = string[-sh:]
        new_string += string[:-sh]
        print(new_string)
        return new_string


def encapsulate(string):
    # empacota a message
    sh = randint(a=0, b=50)
    ori = bool(randint(a=0, b=1))

    if ori:
        new_string = None
        for char in string:
            new_string = ord(char)
            hodler += sh
            new_string = chr(new_string)
        return new_string
    else:
        new_string = string[sh:]
        new_string += string[:sh]
        print(new_string)
        return new_string


def handshake(s):
    # gera criptografia
    pub_key, priv_key = rsa.newKeys(512)

    key = encapsulate(pub_key)
    s.sendall(key)
    their_pub_key = s.recv(1024)
    their_pub_key = desencapsulate(their_pub_key)
    print(their_pub_key + '\n' + pub_key + '\n' + priv_key)
