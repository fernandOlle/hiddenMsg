from typing import Dict
import socket
import sys
from xmlrpc.client import boolean
import rsa
from random import randint
import json
import os

publickey = None
privatekey = None
their_pbkey = None

def desencapsulate(datagram: Dict):
    # desempacota a message
    sh = datagram["shuffle"]
    ori = datagram["orientation"]
    string = datagram["ciphertext"]
    end = datagram["end"]

    if end:
        return "/END"

    new_string = ''
    if ori:
        for char in string:
            holder = ord(char) + sh
            new_string += chr(holder)
    else:
        new_string = string[-sh:]
        new_string += string[:-sh]
    return new_string


def encapsulate(string: str, endChat: boolean):
    # empacota a message
    sh = randint(a=0, b=len(string) - 1)
    ori = bool(randint(a=0, b=1))

    if endChat:
        return {
            "orientation": ori,
            "shuffle": sh,
            "end": True,
            "ciphertext": ""
        }

    new_string = ''
    if ori:
        for char in string:
            holder = ord(char) - sh
            new_string += chr(holder)
    else:
        new_string = string[sh:]
        new_string += string[:sh]

    return {
            "orientation": ori,
            "shuffle": sh,
            "end": False,
            "ciphertext": new_string
        }


def receive(s: socket.socket):
    while True:
        r_msg = s.recv(1024).decode()
        r_msg = json.loads(r_msg)
        r_msg = desencapsulate(r_msg)
        if r_msg == '':
            pass
        if r_msg == '/END':
            print("finalizando conversa...")
            os._exit(0)
        else:
            print('\n' + r_msg)


def send(s: socket.socket):
    while True:
        s_msg = input()#.replace('b', '')
        if s_msg == '':
            pass
        if s_msg == '/END':
            s_msg = encapsulate(s_msg, True)
            s.sendall(json.dumps(s_msg).encode())
            print("finalizando conversa...")
            os._exit(0)
        else:
            s_msg = encapsulate(s_msg, False)
            s.sendall(json.dumps(s_msg).encode())
