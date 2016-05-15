import socket
from deserial2 import *


def registration(s):
    dict1 = {}
    print "enter user name"
    user_name = raw_input()
    print "enter password"
    password = raw_input()
    print "enter date of birth"
    dob = raw_input()
    print "enter mobile number"
    mobile_number = raw_input()
    print "enter email id"
    email = raw_input()
    dict1["option"] = 1
    dict1["user"] = user_name
    dict1["password"] = password
    dict1["dob"] = dob
    dict1["email"] = email
    dict1["mob"] = mobile_number
    dict2 = transport(dict1, s)
    if dict2["msg"] == "error":
        exitfun(s)
    return


def login(s):
    dict1 = {}
    print "enter user name"
    user_name = raw_input()
    print "enter password"
    password = raw_input()
    dict1["option"] = 2
    dict1["user"] = user_name
    dict1["password"] = password
    dict2 = transport(dict1, s)
    if dict2["msg"] == "error":
        return
    while True:
        i=raw_input("do u want to enter 1 for createforum  or 2 for openforum 3 for prev:")
        if i=='1':
            createforum(dict1,s)
        elif i=='2':
            openforum(dict1,s)
        else:
            return


def openforum(dict1, s):
    print "enter forum name"
    forum_name = raw_input()
    dict2 = {}
    dict2["user"] = dict1("username")
    dict2["forum"] = forum_name
    dict2['option']='2'
    dict2 = transport(dict1, s)
    if dict2["msg"] == "error":
        exitfun(s)
    while True:
        i=raw_input("do u want to enter 1 for createsubforum  or 2 for opensubforum 3 for prev:")
        if i=='1':
            createsubforum(dict1,s)
        elif i=='2':
            opensubforum(dict1,s)
        else:
            return


def createforum(dict1, s):
    dict2, dict3 = {}, {}
    print "enter forum name"
    forum_name = raw_input()
    dict2["user"] = dict1["user"]
    dict2["forum"] = forum_name
    dict2['option']='1'
    dict3 = transport(dict2, s)
    if dict3["msg"] == "error":
        exitfun(s)
    while True:
        i=raw_input("do u want to enter 1 for createforum or 2 for openforum 3 for prev:")
        if i=='1':
            createforum(dict1,s)
        elif i=='2':
            openforum(dict1,s)
        else:
           return


def opensubforum(dict1, s):
    dict2 = {}
    subforum = raw_input("enter sub-forum name")
    dict2["user"] = dict1["username"]
    dict2["subforum"] = subforum
    dict2['option']='2'
    dict2 = transport(dict2, s)
    if dict2["msg"] == "error":
        exitfun(s)
    while True:
        i=raw_input("do u want to enter 1 for createquestion  or 2 for openquestion 3 for prev:")
        if i=='1':
            createquestion(dict1,s)
        elif i=='2':
            openquestion(dict1,s)
        else:
            return



def createsubforum(dict1, s):
    dict2, dict3 = {}, {}
    print "enter sub-forum name"
    subforum_name = raw_input()
    dict2["option"] = 1
    dict2["subforum"] = subforum_name
    dict2['option']='1'
    dict3 = transport(dict2, s)
    if dict3["msg"] == "error":
        exitfun(s)
    while True:
        i=raw_input("do u want to enter 1 for createsubforum  or 2 for opensubforum 3 for prev:")
        if i=='1':
            createsubforum(dict1,s)
        elif i=='2':
            opensubforum(dict1,s)
        else:
            return



def openquestion(dict1, s):
    dict2 = {}
    question = raw_input("enter question")
    dict2["user"] = dict1["username"]
    dict2["question"]=question
    dict2['option']='2'
    dict2 = transport(dict2, s)
    if dict2["msg"]=="error":
        exitfun(s)
    while True:
        i=raw_input("do u want to enter 1 for createanswer  2 for prev:")
        if i=='1':
            createanswer(dict1,s)
        else:
            return

def createquestion(dict1, s):
    dict2, dict3 = {}, {}
    print "enter question"
    question = raw_input()
    dict2["user"] = dict1["user"]
    dict2["question"] = question
    dict2['option']='1'
    dict3 = transport(dict2, s)
    if dict3["msg"] == "error":
        exitfun(s)
    while True:
        i=raw_input("do u want to enter 1 for createquestion  or 2 for openquestion 3 for prev:")
        if i=='1':
            createquestion(dict1,s)
        elif i=='2':
            openquestion(dict1,s)
        else:
            return



def createanswer(dict1,s):
    dict2, dict3 = {}, {}
    print "enter answer"
    answer = raw_input()
    dict2["user"] = dict1["user"]
    dict2["answer"] = answer
    dict2['option']='1'
    dict3 = transport(dict2, s)
    while True:
        i=raw_input("do u want to enter 1 for createanswer  or 2 for prev:")
        if i=='1':
            createanswer(dict1,s)
        return



def displayforum(s):
    dict1 = []
    dict1["option"] = 3
    dict2 = transport(dict1, s)
    if dict2["msg"] == "noforums":
        return
    else:
        forums(s)
    return


def question(s):
    dict1 = {}
    questions = raw_input("enter question name")
    dict1["questions"] = questions
    transport(dict1, s)
    return


def subforums(s):
    dict1 = {}
    subforum = raw_input("enter sub-forum name")
    dict1["subforum"] = subforum
    dict2 = transport(dict1, s)
    if dict2["msg"] != "noquestions":
        question(s)
    return


def forums(s):
    dict1 = []
    forum = raw_input("enter forum name")
    dict1["forum"] = forum
    dict2 = transport(dict1, s)
    if dict2[0] != "nosubforums":
        subforums(s)
    return



def transport(dict1, s):
    length = len(str(dict1))
    length = len(str(length) + str(dict1))
    msg = str(length) + str(dict1)
    s.send(msg)
    l1 = []
    k = 0
    while (True):
        length = s.recv(1)
        if not (ord(length) >= ord('0') and ord(length) <= ord('9')):
            l1.append(length)
            break
        k = k * 10 + ord(length) - ord('0')
    msg = s.recv(k)
    l1.append(msg)
    msg = "".join(l1)
    i, dict2 = deserialize(msg, 0)
    print dict2
    return dict2



def socket1(s):
    while(True):
        i = raw_input("enter input 1 for registration 2 for login 3 for display forums:")
        if i == '1':
            registration(s)
        elif i == '2':
            login(s)
        else:
            displayforum(s)
        i=raw_input("press 1 for exit or 2 for no")
        if i=='1':
         s.close()




def exitfun(s):
    i = raw_input("wanna to go to main console")
    if i == 'y':
        socket1(s)
    else:
        s.close()
        exit(1)



def socket2():
    print "entered in  to group6 forum"
    s = socket.socket()
    s.connect(('localhost', 8083))
    socket1(s)



socket2()