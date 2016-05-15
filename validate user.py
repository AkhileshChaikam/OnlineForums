__author__ = 'Shrikita'
import string
from bottle import route, run, request, get, post, response
from project_new import *

class cache():
    def __init__(self):
        self.io=iofile()
        self.list_cache=self.io.getusernames()
    def add_username(self,d):
        for u in self.list_cache:
            if(u==d["username"]):
                return "username exists"
        self.io.create_user(d)
        return "signup sucessful"
@route("/login",method="POST")
def login():
    d={}
    d["username"]=request.POST("username")



@route('/signup',method='POST')
def validateuser():
    d={}
    d["username"]=request.POST['username']
    for i in d["username"]:
        if(i not in string.ascii_letters and i not in string.digits and i!="_"):
            return "username not valid"
    d["email"]=request.POST['email']
    if("@" not in d["email"]):
        return "email not valid"
    if(not d["email"].endswith(".com")):
        return "email not valid"
    d["mobilenumber"]=request.POST['mobilenumber']
    if(len(d["mobilenumber"])!=10):
        return "mobilenumber not valid"
    for i in d["mobilenumber"]:
        if(i not in string.digits):
            return "mobilenumber not valid"
    d["password"]=request.POST['password']
    if(len(d["password"])>10):
        return "password too long"
    d["dob"]=request.POST['dob']
    l=d["dob"].split("-")
    if(len(l[0])!=4or (len(l[1])!=2) or (len(l[2])!=2)):
        return "date of birth not valid"
    else:
        try:
            int(l[0])
            int(l[1])
            int(l[2])
        except ValueError:
            return "date of birth not valid"
    obj=cache()
    obj.add_username(d)
run(host='localhost', port=8083, debug=True, reloader=True)
