import socket


def socket2():
    print "entered in  to group6 forum"
    s = socket.socket()	
    s.connect(('127.0.0.10', 8083))
    transport("connected", s)


def transport(msg, s):
    while (True):
        length = len(msg)
        msg = str(length) + str('/') + msg
        s.send(msg)
        l1 = []
        k = 0
        while (True):
            length = s.recv(1)
            if (length == '/'):
                break
            k = k * 10 + ord(length) - ord('0')
        msg = ""
        msg = s.recv(k)
        if msg == "exit":
            s.close()
        if msg != "error":
            msg = raw_input(msg)
        else:
            print "error"


socket2()