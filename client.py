import urllib2
import datetime
import urllib
def registration():
    dr={}
    '''print "first name"
    first_name=raw_input()
    print "last name"
    last_name=raw_input()'''
    print "enter user name"
    user_name=raw_input()
    dr['username']=user_name
    print "enter password"
    password=raw_input()
    '''print "enter reenter password"
    reenter_password=raw_input()'''
    print "enter date of birth"
    dob=raw_input()
    '''print "enter gender"
    gender=raw_input()'''
    print "enter mobile number"
    mobile_number=raw_input()
    print "enter email id"
    email=raw_input()
    '''now = datetime.datetime.now()
    temp=now.date()
    date=str(temp)'''
    #dr['first_name']=first_name
    #dr['last_name']=last_name
    dr['username']=user_name
    dr['password']=password
    #dr['reenter_password']=reenter_password
    dr['dob']=dob
    #dr['gender']=gender
    dr['mobilenumber']=mobile_number
    dr['email']=email
    #dr['date']=date
    #print dr
    return dr
def login():
    dl={}
    print "enter user name"
    user_name=raw_input()
    print "enter password"
    password=raw_input()
    dl['username']=user_name
    dl['password']=password
    return dl
print "enter ur option 1)registration 2)login"
i=raw_input()
if i=='1':
    print "enter ur registration details"
    dr=registration()
    databytes = urllib.urlencode(dr)
    req = urllib2.urlopen(url='http://localhost:8083/signup', data=databytes.encode('utf-8'))
    print(req)
else:
    print "enter ur login details"
    dl=login()
    databytes = urllib.urlencode(dl)
    req = urllib2.urlopen(url='http://localhost:8083/login', data=databytes.encode('utf-8'))