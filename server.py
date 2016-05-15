__author__ = 'Shrikita'
import socket
from deserialiser import *
from project_new import *
import string
def splitdate(s):
    l=[]
    tl=[]
    for i in range(len(s)):
        if(s[i]=="-"):
            tl="".join(tl)
            l.append(tl)
            tl=[]
        else:
            tl.append(s[i])
    else:
        tl="".join(tl)
        l.append(tl)
    return l
def receive(s):
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
    i, d = deserialize(msg, 0)
    return d
def transport(d, s):
    length = len(str(d))
    length = len(str(length) + str(d))
    msg = str(length) + str(d)
    s.send(msg)
class cache():
    def __init__(self):
        self.io=file()
        self.list_cache=self.io.getusernames()
    def add_username(self,d):
        for u in self.list_cache:
            if(u==d["user"]):
                return "username exists"
        self.io.create_user(d)
        return "signup sucessful"
def loggedin(c):

    f=[]#forumnames
    d={}
    for i in len(f):
        d[i]=f[i]
    transport(d,c)
    while(True):
        d=receive(c)
        try:
            if d["option"]=="1":
                for i in d["forum"]:
                    if(i not in string.ascii_letters and i not in string.digits and i!="_"):
                        d["msg"]="error"
                        transport(d,c)
                        raise Exception("")
                f=[]#forumnames
                for i in f:
                    if(i==d["forum"]):
                        d["msg"]="error"
                        transport(d,c)
                        raise Exception("")
            #createforum()
            elif d["option"]=="2":
                sf=[]#subforum
                d={}
                for i in len(sf):
                   d[i]=sf[i]
                transport(d,c)
                d=receive(c)
                while(True):
                    if(d["option"]=="1"):
                        flag=0
                        for i in f:
                            if(i==d["forum"]):
                                flag=1
                                break
                        if(flag==0):
                            d["msg"]="error"
                            transport(d,c)
                            raise Exception("")
                        for i in d["subforum"]:
                            if(i not in string.ascii_letters and i not in string.digits and i!="_"):
                                d["msg"]="error"
                                transport(d,c)
                                raise Exception("")
                        sf=[]#subforum
                        for i in sf:
                            if(i==d["subforum"]):
                                d["msg"]="error"
                                transport(d,c)
                                raise Exception("")
                        #create subforum
                    elif(d["option"]=="2"):
                        q=[]#getquestions
                        d={}
                        for i in len(q):
                            d[i]=q[i]
                        transport(d,c)
                        d=receive(c)
                        while(True):
                            if(d["option"]=="1"):pass
                                #create question
                            elif(d["option"]=="2"):
                                d=receive(c)
                                a=[]#getanswers
                                d={}
                                for i in len(a):
                                    d[i]=a[i]
                                transport(d,c)
                                d=receive(c)
                                if(d["option"]=="1"):pass
                                    #answer
                                elif(d["option"]=="2"):
                                    pass
                            elif(d["option"]=="3"):
                                break
                    elif(d["option"]=="3"):
                        break
            elif(d["option"]=="3"):
                return
        except Exception:
            pass

def client():
    s=socket.socket()
    host="localhost"
    port=8083
    s.bind((host,port))
    s.listen(5)
    c,address=s.accept()
    print "abc"
    while(True):
        try:
            d=receive(c)
            print "ab"
            if(d["option"]=="1"):
                print "server"
                for i in d["user"]:
                    if(i not in string.ascii_letters and i not in string.digits and i!="_"):
                        d["msg"]="error"
                        transport(d,c)
                        raise Exception("")
                if("@" not in d["email"]):
                    d["msg"]="error"
                    transport(d,c)
                    raise Exception("")
                if(len(d["mob"])!=10):
                    d["msg"]="error"
                    transport(d,c)
                    raise Exception("")

                for i in d["mob"]:
                    if(i not in string.digits):
                        d["msg"]="error"
                        transport(d,c)
                        raise Exception("")
                if(len(d["password"])>10):
                    d["msg"]="error"
                    transport(d,c)
                    raise Exception("")
                dl=splitdate(d["dob"])
                if(len(dl[0])!=4or (len(dl[1])!=2) or (len(dl[2])!=2)):
                    d["msg"]="error"
                    transport(d,c)
                    raise Exception("")
                else:
                    try:
                        int(dl[0])
                        int(dl[1])
                        int(dl[2])
                    except ValueError:
                        d["msg"]="error"
                        transport(d,c)
                        raise Exception("")
                obj=cache()
                del d["option"]
                obj.add_username(d)
                d["msg"]="registration sucessful"
                transport(d,c)
            elif(d["option"]=="2"):
                up=[[]]
                for i in range(len(up)):
                    if(d["user"]==up[i][0]):
                        if(d["password"]==up[i][1]):
                            d["msg"]="sucessful"
                            transport(d,c)
                            loggedin(c,up[1])
                        else:
                            d["msg"]="error"
                            transport(d,c)
                            raise Exception("")
                d["msg"]="error"
                transport(d,c)
                raise Exception("")
            elif(d["option"]=="3"):
                f=[]#forumnames
                d={}
                for i in len(f):
                   d[i]=f[i]
                transport(d,c)
                d=receive(c)
                if(d["forum"] not in f):
                    d["msg"]="noforums"
                    raise Exception("")
                sf=[]#getsubforums(d["forum"])
                d={}
                for i in len(sf):
                   d[i]=sf[i]
                transport(d,c)
                d=receive(c)
                if(d["subforum"] not in sf):
                    d["msg"]="nosubforums"
                    raise Exception("")
                q=[]#getquestions
                d={}
                for i in len(q):
                   d[i]=q[i]
                transport(d,c)
                d=receive(c)
                if(d["questions"] not in q):
                    raise Exception("")
                a=[]#getanswers
                d={}
                for i in len(a):
                   d[i]=a[i]
                transport(d,c)
        except Exception:
            pass
client()