__author__ = 'mani sowndarya'
import struct
class cache():
    def __init__(self):
        list_cache=[]#initialize with the usernames
    def add_username(self,d):
        for u in self.list_cache:
            if(u==d["username"]):
                return "username exsits"
        #call the i/o
        return "signup sucessful"
    def getstring(self,s):
        for i in range(len(s)):
            if(s[i]=="\x00"):
                return s[:i]
    def getforumnames(self):
        fn=[]
        self.f.seek(9,0)
        t=self.f.read(4)
        t,=struct.unpack("i",t)
        self.f.seek(1024,0)
        for i in range(t):
            f1=self.f.read(30)
            f1=self.getstring(f1)
            fn.append(f1)
            self.f.seek(4,1)
        return fn
    def create1(self,d1):
        for f1 in self.fn:
            if (f1==d1["forumname"]):
                return "forumname exists"
            #call the i/o
            return "forumname created"
    def display(self,d2):
        keys_list=[]
        keys_list=d2.keys()
        return keys_list

