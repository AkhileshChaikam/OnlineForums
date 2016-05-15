__author__ = 'Shrikita'
import struct
def strip(s):
    l=[]
    for i in range(len(s)):
        if(s[i]=="\x00"):
            return "".join(l)
        else:
            l.append(s[i])
class file():
   def __init__(self):
        self.f=open("gbbinaryfile.bin","rb+")
        self.stack=[]
        self.userstack=[]
        self.f.seek(4,0)
        if self.f.read(1)!="1":
            self.init()
        self.stack.append(self.load(5,30,3072))
        self.userstack.append(self.load(9,30,1024))
        self.password=self.getpasswords([30,20,30,10,10,500],self.userstack)
   def init(self):
        self.i=1
        self.f.seek(0,0)
        while self.i<1024*1024:
            self.f.seek(1020,1)
            t=struct.pack("i",self.i)
            self.i+=1
            self.f.write(t)
        self.f.seek(0,0)
        t=struct.pack("i",1)
        self.f.write(t)
        self.f.write("1")
        t=struct.pack("i",0)
        self.f.write(t)
        self.f.write(t)

   def create_block(self):
        self.f.seek(0,0)
        t=self.f.read(4)
        n,=struct.unpack("i",t)
        self.f.seek(n*1024+1020,0)
        t=self.f.read(4)
        self.f.seek(0,0)
        self.f.write(t)
        return n
   def checkduplicate(self,stack,d):
       for j in stack[-1][0]:
            if(d==j):
                return -1
       return 1
   def create(self,size,d,s,count,f,stack):
        m=1020/(size+4)
        i=len(stack[-1][0])%m
        if i==0:
            b=self.create_block()
            if(len(stack[-1][1])==0):
                if(f==1):
                    self.f.seek(count+1020)
                    b1=struct.pack("i",b)
                    self.f.write(b1)
            else:
                self.f.seek(stack[-1][1][-1]*1024+1020)
                b1=struct.pack("i",b)
                self.f.write(b1)
            stack[-1][1].append(b)
        self.f.seek(stack[-1][1][-1]*1024+i*(size+4),0)
        self.f.write(d[0])
        t=self.create_block()
        stack[-1][0].append(d[0])
        stack[-1][2].append(t)
        n=struct.pack("i",t)
        self.f.seek(stack[-1][1][-1]*1024+i*(size+4)+size,0)
        self.f.write(n)
        self.f.seek(t*1024,0)
        n=struct.pack("i",0)
        self.f.write(n)
        x=0
        for i in range(len(d)):
            self.f.seek(4+x+t*1024,0)
            self.f.write(d[i])
            x=x+s[i]
        self.f.seek(count,0)
        n=struct.pack("i",len(stack[-1][0]))
        self.f.write(n)
        #self.f.flush()
   def load(self,count,size,base):
       l1=[]
       l2=[]
       l3=[]
       self.f.seek(count)
       n=self.f.read(4)
       n,=struct.unpack("i",n)
       m=1020/(size+4)
       while(len(l1)!=n):
           l2.append(base/1024)
           self.f.seek(base)
           for i in range(m):
               l1.append(strip(self.f.read(size)))
               t=self.f.read(4)
               t,=struct.unpack("i",t)
               l3.append(t)
               if(len(l1)==n):
                   break
           else:
               self.f.seek(base+1020)
               t=self.f.read(4)
               t,=struct.unpack("i",t)
               base=t*1024
       return [l1,l2,l3]


   def retrive(self,no,size,stack):
        if len(stack[-1][0])<no:
            return -1,"error"
        else:
            b=stack[-1][2][no-1]*1024
            self.f.seek(stack[-1][2][no-1]*1024,0)
            n=self.f.read(4)
            n,=struct.unpack("i",n)
            l1=[]
            l2=[]
            l3=[]
            if(n>0):
                self.f.seek(stack[-1][2][no-1]*1024+1020,0)
                r=self.f.read(4)
                r,=struct.unpack("i",r)
                l2.append(r)
                m=1020/(size+4)
                i=0
                while(i<n):
                    for j in range(m):
                        self.f.seek(r*1024+j*(size+4))
                        l1.append(strip(self.f.read(size)))
                        t=self.f.read(4)
                        t,=struct.unpack("i",t)
                        l3.append(t)
                        i=i+1
                        if(i==n):
                            break
                    else:
                        self.f.seek(l2[-1]*1024+1020)
                        r=self.f.read(4)
                        r,=struct.unpack("i",r)
                        l2.append(r)
            l=[]
            l.append(l1)
            l.append(l2)
            l.append(l3)
            stack.append(l)
            l=[]
            for i in range(len(l1)):
                l.append("{} {}".format(i+1,l1[i]))
            return b,"\n".join(l)
   def metadataretrive(self,s,no,stack):
        if len(stack[-1][0])<no:
            return "error"
        else:
            b=stack[-1][2][no-1]*1024
            t=0
            l=[]
            for i in s:
                self.f.seek(b+4+t)
                l.append(self.f.read(i))
                t=t+i
        return "\n".join(l)
   def getpasswords(self,s,stack):
       l=[]
       for no in range(len(stack[-1][0])):
            b=stack[-1][2][no]*1024
            t=0
            for i in range(len(s)):
                if(i==1):
                    self.f.seek(b+4+t)
                    l.append(strip(self.f.read(s[i])))
                    break
                t=t+s[i]
       return l



import socket
from validate import *

def getallforums():
    l=[]
    for i in range(len(io.stack[0][0])):
        l.append("{} {}".format(i+1,io.stack[0][0][i]))
    return "\n".join(l)
def find(u,p,ul,pl):
    for i in range(len(ul)):
        if(ul[i]==u):
            if(pl[i]==p):
                return "login sucessful"
            else:
                return "error"
    return "error"
def registration(s):
    user_name=transport("enter user name",s)
    if uname(user_name)=='error':
        i=transport("error press 1 for exit or 2 for no:",s)
        return i
    f=io.checkduplicate(io.userstack,user_name)
    if(f==-1):
        i=transport("error press 1 for exit or 2 for no:",s)
        return i
    password=transport ("enter password",s)
    if pwd(password)=='error':
        i=transport("error press 1 for exit or 2 for no:",s)
        return i
    email=transport ("enter email",s)
    if email1(email)=="error":
        i=transport("error press 1 for exit or 2 for no:",s)
        return i
    dob=transport ("enter dob",s)
    if dob1(dob)=="error":
        i=transport("error press 1 for exit or 2 for no:",s)
        return i
    mob=transport ("enter mobile number",s)
    if mob1(mob)=="error":
        i=transport("error press 1 for exit or 2 for no:",s)
        return i
    list1=[]
    list1.append(user_name)
    list1.append(password)
    list1.append(email)
    list1.append(dob)
    list1.append(mob)
    io.create(30,list1,[30,20,30,10,10],9,0,io.userstack)
    io.password.append(password)
    i=transport("succesfully registered ..press 1 for exit any other key for no",s)
    return i


def login(s):
    user_name=transport ("enter user name",s)
    if uname(user_name)=='error':
        i=transport("error press 1 for exit or 2 for no:",s)
        return i
    password=transport ("enter password",s)
    if pwd(password)=='error':
        i=transport("error press 1 for exit or 2 for no:",s)
        return i
    i=find(user_name,password,io.userstack[0][0],io.password)
    if i=='error':
        i=transport("error press 1 for exit or 2 for no:",s)
        return i
    while True:
        i=transport("login successful \n"+getallforums()+ "\n do u want to enter 1 for createforum  or 2 for openforum any other key for prev:",s)
        if i=='1':
            createforum(user_name,s)
        elif i=='2':
            openforum(user_name,s)
        else:
            return


def openforum(username, s):
    while(True):
        forumno=transport("enter forum_no",s)
        forumno=int(forumno)
        b,sub=io.retrive(forumno,30,io.stack)
        if(b!=-1):
            break
        else:
            i=transport("wrong input enter 1 to reenter or 2 for return",s)
            if(i=="2"):
                return

    while(True):
     i=transport(sub+"\ndo u want to enter 1 for createsubforum or2for opensubforum any other key for prev",s)
     while True:
        if i=='1':
            createsubforum(username,s,b,sub)
        elif i=='2':
            opensubforum(username,s)
        else:
            io.stack.pop()
            return


def createforum(username, s):
    while(True):
     forum_name = transport("enter forum name",s)
     i=io.checkduplicate(io.stack,forum_name)
     if i==1:
         break
     i=transport("name already exist press 1 for reenter forumname any other key for prev ",s)
     if i=="2":
         return
    desc=transport("enter descrption",s)
    io.create(30,[forum_name,desc,username],[30,500,30],5,0,io.stack)
    while True:
        i=transport("creation succesful\n"+getallforums()+" \ndo u want to enter 1 for createforum or 2 for openforum any other key for prev:",s)
        if i=='1':
            createforum(username,s)
        elif i=='2':
            openforum(username,s)
        else:
           return


def opensubforum(username, s):

    while(True):
        subforum_no = transport("enter sub-forum no",s)
        subforum_no=int(subforum_no)
        b,p=io.retrive(subforum_no,100,io.stack)
        if(b!=-1):
            break
        else:
            i=transport("wrong input enter 1 to reenter or 2 key for return",s)
            if(i=="2"):
                return
    while True:
        i=transport(p+"\ndo u want to enter 1 for createquestion  or 2 for openquestion any other key for prev:",s)
        if i=='1':
            createquestion(username,s,b,p)
        elif i=='2':
            openquestion(username,s)
        else:
            io.stack.pop()
            return



def createsubforum(username, s,b,sub):
    while(True):
     subforumname = transport("enter sub-forum name",s)
     i=io.checkduplicate(io.stack,subforumname)
     if i==1:
         break
     i=transport("name already exist press 1 for reenter forumname 2 key for prev ",s)
     if i=="2":
         return
    desc=transport("enter descrption",s)
    io.create(30,[subforumname,username,desc],[30,30,500],b,1,io.stack)
    while True:
        i=transport("creation succesful\n"+sub+" \ndo u want to enter 1 for createsubforum  or 2 for opensubforum any other key for prev:",s)
        if i=='1':
            createsubforum(username,s,b,sub)
        elif i=='2':
            opensubforum(username,s)
        else:
            return



def openquestion(username, s):
    while(True):
        no = transport("enter question no",s)
        no=int(no)
        b,p=io.retrive(no,100,io.stack)
        if(b!=-1):
            break
        else:
            i=transport("wrong input enter 1 to reenter or 2 key for return",s)
            if(i=="2"):
                return
    while True:
        i=transport(p+"\ndo u want to enter 1 for createanswer  any other key for prev:",s)
        if i=='1':
            createanswer(username,s,b,p)
        else:
            io.stack.pop()
            return

def createquestion(username, s,b,p):
    while(True):
     q = transport("enter question",s)
     i=io.checkduplicate(io.stack,q)
     if i==1:
         break
     i=transport("question already exist press 1 for reenter question 2 key for prev ",s)
     if i=="2":
         return
    desc=transport("enter descrption",s)
    io.create(100,[q,username,desc],[100,30,800],b,1,io.stack)
    while True:
        i=transport("question created succesuful\n"+p +"\ndo u want to enter 1 for createquestion  or 2 for openquestion any other key for prev:",s)
        if i=='1':
            createquestion(username,s,b,p)
        elif i=='2':
            openquestion(username,s)
        else:
            return



def createanswer(username,s,b,p):
    while(True):
     q = transport("enter answer",s)
     i=io.checkduplicate(io.stack,q)
     if i==1:
         break
     i=transport("answer already exist press 1 for reenter question 2 key for prev ",s)
     if i=="2":
         return
    desc=transport("enter descrption",s)
    io.create(100,[q,username,desc],[100,30,800],b,1,io.stack)
    while True:
        i=transport(p+"\ndo u want to enter 1 for createanswer  or any other key for prev:",s)
        if i=='1':
            createanswer(username,s,b,p)
        return



def displayforum(s):
    while(True):
      i=transport(getallforums()+" \nenter forum no to enter", s)
      forums(int(i),s)
      i=transport("wrong input enter 1 for reenter 2 for prev:",s)
      if i=='2':
          return


def question(question1,s):
   b,p=io.retrive(question1,100,io.stack)
   if b==-1:
       return -1
   transport(p+"\nenter a key to go back",s)
   io.stack.pop()
   return 1



def subforums(subforum,s):
    b,p=io.retrive(subforum,100,io.stack)
    if b==-1:
        return -1
    while(True):
     question1 = transport(p+"\n enter question no",s)
     w=question(int(question1),s)
     if w==1:
        i=transport("1 for go to prev any other key to  continue",s)
        if i=='1':
            io.stack.pop()
            return 1
     else:
         i=transport("wrong input enter 1 for reenter 2 for prev:",s)
         if i=='2':
            io.stack.pop()
            return 1


def forums(forumno,s):
    b,p=io.retrive(forumno,30,io.stack)
    if(b==-1):
        return -1
    while(True):
     subforum = transport(p+"\nenter sub forum no",s)
     w=subforums(int(subforum),s)
     if w==1:
        i=transport("1 for go to prev any other key to continue",s)
        if i=='1':
            io.stack.pop()
            return
     else:
         i=transport("wrong input enter 1 for reenter 2 for prev:",s)
         if i=='2':
            io.stack.pop()
            return 1


def transport(string1, c):
    length = len(string1)
    msg = str(length) +str('/')+ str(string1)
    c.send(msg)
    l1 = []
    k = 0
    while (True  and msg!="4/exit"):
        length = c.recv(1)
        if  (length=='/'):
            break
        k = k * 10 + ord(length) - ord('0')
    if k!=0:
     msg = c.recv(k)
    return msg



def socket1(s):
    while(True):
        i="enter input 1 for registration 2 for login 3 for display forums any other key for exit:"
        i=transport(i,s)
        if i == '1':
            i=registration(s)
        elif i == '2':
            i=login(s)
        elif i == '3':
            i=displayforum(s)
        else:
            i=transport("exit",s)
            s.close()
            exit(0)
        if i=='1':
         transport("exit",s)
         s.close()
         exit(0)





def socket2():
    print "entered in  to group6 forum"
    s = socket.socket()
    s.bind(('127.0.0.10', 8083))
    s.listen(5)
    c, addr = s.accept()
    msg=c.recv(1024)
    if msg=="9/connected":
        socket1(c)
    else:
        c.close()

io=file()
#b,sub=io.retrive(1,30,io.stack)
#b,p=io.retrive(1,100,io.stack)
#b,p=io.retrive(1,100,io.stack)
#for i in range(99):
#    io.create(100,["answer{}".format(i),"abhinand","decription"],[100,30,800],b,1,io.stack)
#io.create(30,["cricket","game","akilesh"],[30,500,30],5,0,io.stack)
#io.create(30,["abhinand","123456","abhinand@gmail.com","1992-12-12","9848022338","leader"],[30,20,20,10,10,500],9,0,io.userstack)

#print find("abhinand","123456",io.userstack[0][0],io.password)
socket2()