def getvalue(s,i):
    if(s[i]=="'"):
        i=i+1
        l=[]
        while(s[i]!="'"):
            l.append(s[i])
            i=i+1
        else:
            i=i+1
            value="".join(l)
    elif(s[i]=="N"):
        value=None
        i=i+4
    elif(s[i]=="["):
        value,i=delist(s,i)
        i=i+1
    else:
        l=[]
        while(s[i]!="," and s[i]!="}" and s[i]!=" " and s[i]!=":" and s[i]!="]"):
            l.append(s[i])
            i=i+1
        else:
            t="".join(l)
            value=int(t)
    return value,i
def delist(l,i):
    m=[]
    if(l[i]=="["):
        i=i+1
        while(l[i]!="]"):
            while(l[i]==" "):
                i=i+1
            else:
                if(l[i]=="{"):
                    i,d=deserialize(l,i)
                    m.append(d)
                elif(l[i]==","):
                        i=i+1
                elif(l[i]=="}"):
                    i=i+1
                elif(l[i]=="]"):
                    break
                else:
                    val,i=getvalue(l,i)
                    m.append(val)
    return m,i
def deserialize(s,i):
    d={}
    while(s[i]==" "):
        i=i+1
    else:
        if(s[i]=="{"):
            i=i+1
            while(s[i]!="}"):
                if(s[i]==","):
                    i=i+1
                while(s[i]==" "):
                    i=i+1
                else:
                    key,i=getvalue(s,i)
                while(s[i]==" "):
                    i=i+1
                else:
                    if(s[i]==":"):
                        i=i+1
                        while(s[i]==" "):
                            i=i+1
                        else:
                            value,i=getvalue(s,i)
                d[key]=value
                while(s[i]==" "):
                    i=i+1
    return i,d
#print deserialize("{'content': None, 'message': None, 'option': None, 'forum': None, 'noofchunks': None}",0)
#print deserialize("{0: [{0: '1234', 1: 'asdfg'}, {0: 3, 4: 'eow'}], 'abc': 'asd'}",0)
#print delist("[{'sai':'571'},{'sunny':'572'}]",0)

#print deserialize("{'messages': [{0: 'asdf'}], 'command': 'create', 'name': 'abhi'}",0)