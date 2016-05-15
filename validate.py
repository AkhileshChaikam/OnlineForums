__author__ = 'Shrikita'

def find_length(str1):
    len1=0
    for char in str1:
        len1+=1
    return len1


def validname(s):
    for i in s:
        if not (ord(i)>=ord("a") and ord(i)<=ord("z") or (ord(i)>=ord("A") and ord(i)<=ord("Z")) or (ord(i)>=ord("0") and ord(i)<=ord("9")) or ord(i)==ord("_")):
            return False
    return True
def uname(s):
    if(len(s)>20 or len(s)<6):
        return "error"
    if validname(s):
        return "valid username"
    else:
        return "error"
def pwd(s):
    if(len(s)>10 or len(s)<6):
        return "error"
    else:
        return "valid password"
def find(u,p,ul,pl):
    for i in range(len(ul)):
        if(ul[i]==u):
            if(pl[i]==p):
                return "login sucessful"
            else:
                return "error"
    return "error"
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
    if not (l[0]>="1863" and l[0]<="2013"):
        return "error"
    elif not (l[1]>="1" and l[1]<="12"):
        return "error"
    elif not (l[2]>="1" and l[2]<="31"):
        return "error"
    else:
        return l


def dob1(d):
    l=splitdate(d)
    if(len(l[0])!=4 or len(l[1])!=2 or len(l[2])!=2 or len(d)!=10):
        return "error"
    else:
        return "valid date"

		
def email1(input):
    l=find_length(input)
    flag=0
    for i in range(l):
        if input[i]=='@':
            flag=1
            break
    if(flag==1):
        if(input[l-1]=="m"):
            if(input[l-2]=="o"):
                if(input[l-3]=="c"):
                    if(input[l-4]=="."):
                        return "email is valid"
    return "error"

def mob1(input):
    l=find_length(input)
    if l==10:
        for i in range(l):
            if i==0:
                if input[i]=='0':
                    return "error"
            if ord(input[i])>=48 and ord(input[i])<=57:
                continue
            else:
                return "error"
    else:
         return "error"
    return "valid mobile number "

j=splitdate("2012-11-45")
print j