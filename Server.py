from socket import *
import _thread
from AESobjectfile import AESCipher


key = "0123456789abcdef"


def on_new_client(clientsocket, addr):
    while True:
        msg = clientsocket.recv(1024)
        # do some checks and if msg == someWeirdSignal: break:
        if not msg:
            break
        print(addr, ' >> ', msg)
        # msg = raw_input('SERVER >> ')
        # Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg)
    clientsocket.close()


HOST = ""   # localhost
PORT = 65432


s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)

print("Server is running")


# conn, addr = s.accept()
# print(addr, "is connected")
# while 1:
#    data = conn.recv(1024)
#    if not data:
#        break
#    a = AESCipher(key)
#    msg = a.decrypt(data)
#    print("Received Message", repr(msg))
#    if msg == "q" or "Q":
#        s.close()

while True:
    c, addr = s.accept()     # Establish connection with client.
    print("Established connection with", addr, "at port", c.proto)
    _thread.start_new_thread(on_new_client,(c,addr))
    # Note it's (addr,) not (addr) because second parameter is a tuple
    # Edit: (c,addr)
    # that's how you pass arguments to functions when creating new threads using thread module.