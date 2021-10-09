from socket import *
from AESobjectfile import AESCipher


key = "0123456789abcdef"
a = AESCipher(key)


s = socket(AF_INET, SOCK_STREAM)
s.connect(("", 65432))
# a = AESCipher(key)
# text = "Q"
# e = a.encrypt(text)
# s.send(e)


def receive():
    msg = s.recv(1024)
    # a = AESCipher(key)
    d = a.decrypt(msg)
    print("Received Message : ", d)


def send():
    # "Enter the message to be sent : "
    msg = input("Enter the message to be sent : ")
    # a = AESCipher(key)
    e = a.encrypt(msg)
    s.send(e)


while True:
    # print("Enter 1 to send message and 'q' or 'Q' to close")
    opt = input("Enter 1 to send message and 'q' or 'Q' to close : ")
    if opt == '1':
        send()
    elif opt == 'q' or 'Q':
        s.close()
    receive()
