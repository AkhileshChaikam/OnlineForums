__author__ = 'Poornima'
import struct
class iofile():
    def __init__(self):
        self.f=open("gbbinaryfile2.obj","wb+")
        self.f.seek(4,0)
        if self.f.read(1)!="1":
            self.init()

    def init(self):
        i=1
        self.f.seek(0,0)
        while i<1024*1024:
            self.f.seek(1020,1)
            t=struct.pack("i",i)
            self.f.write(t)
            i+=1
        self.f.seek(0,0)
        t=struct.pack("i",3)
        self.f.write(t)
        self.f.write("1")
        t=struct.pack("i",0)
        self.f.write(t)
        self.f.write(t)

    def create_block(self):
        self.f.seek(0,0)
        t=self.f.read(4)
        temp,=struct.unpack("i",t)
        temp=temp*1024
        self.f.seek(temp+1020,0)
        str1=self.f.read(4)
        self.f.seek(0,0)
        self.f.write(str1)
        return temp
    def getstring(self,s):
        for i in range(len(s)):
            if(s[i]=="\x00"):
                return s[:i]
    def getusernames(self):
        un=[]
        self.f.seek(5,0)
        t=self.f.read(4)
        t,=struct.unpack("i",t)
        self.f.seek(1024,0)
        for i in range(t):
            u=self.f.read(20)
            u=self.getstring(u)
            un.append(u)
            self.f.seek(4,1)
        return un


    def create_user(self,dict1):
        self.f.seek(5,0)
        t=self.f.read(4)
        t,=struct.unpack("i",t)
        t=t+1
        self.f.seek(5,0)
        tmp=struct.pack("i",t)
        self.f.write(tmp)
        temp=self.create_block()
        self.f.seek((t-1)*24+1024,0)
        self.f.write(dict1['username'])
        self.f.seek((t-1)*24+1024+20,0)
        t=struct.pack("i",temp)
        self.f.write(t)
        self.f.seek(temp,0)
        self.f.write(str(dict1))

if __name__ == "__main__":
    obj=iofile()
    print obj.getusernames()
    #dict1={"username":"siva", "password":"hello","mail":"siva@gmail.com","DOB":"1-1-1992","phone":9949991715}
    #obj.create_user(dict1)
    obj.f.close()
