import pgpy
from pgpy.constants import *
from random import randint


publickey = None

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
    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 1024)
    key = encapsulate(key)
    s.sendall(key)
    publickey = s.recv(1024)
    publickey = desencapsulate(publickey)
