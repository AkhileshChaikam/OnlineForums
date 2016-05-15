__author__ = 'mani sowndarya'
import io_module
def find_length(self,str):
    len=0
    for char in str:
        len+=1
    return len

class memory_data_structure(object):
    def __init__(self):
        self.usernames=[[None]]*1000
        self.forumnames=[[None]]*100
        self.question=[[None]]*2000


    def hash_function(self,string,size):
        length=find_length(string)
        sum=0
        i=0
        while i < length:
            j=0
            product=1
            sum1=0
            while j < 3 and (i+j) < length:
                sum1 +=ord(string[i+j])*product
                product*=256
                j+=1
            sum+=sum1
            i+=j
        return sum%size


    def get_forum(self,name):
        p=self.hash_func(name,30)
        if self.forumnames[p]==[None]:
            return None
        else:
            list=self.forumnames[p]
            i=0
            len=find_length(list)
            while i < len:
                if list[i][1] == name:
                    return 'Already exists'
                i+=1
            return None
    def get_user(self,name):
        p=self.hash_func(name,1000)
        if self.usernames[p]==[None]:
            return None
        else:
            list=self.usernames[p]
            i=0
            len=find_length(list)
            while i < len:
                if list[i][1] == name:
                    return 'Already exists'
                i+=1
            return None
    def get_question(self,name):
        p=self.hash_func(name,2000)
        if self.questions[p]==[None]:
            return None
        else:
            list=self.questions[p]
            i=0
            len=self.find_length(list)
            while i < len:
                if list[i][1] == name:
                    return 'Already exists'
                i+=1
            return None

    def __init__users(self):
        args=get_users_from_io()
        self.usernames=[[None]]
        i=0
        size=1000
        if args!=None:
            while i<find_length(args):
                name = args[i][0]
                p=self.hash_func(name,size)
                if self.usernames[p]==None:
                    self.usernames[p]=[args][i]
                else:
                    self.usernames[p].append(args)
                i=i+1


    def __init__forums(self):
        args=get_forums_io()
        self.forumnames=[[None]]
        i=0
        size=100
        if args!=None:
            while i<find_length(args):
                name = args[i][0]
                p=self.hash_func(name,size)
                if self.forumnames[p]==None:
                    self.forumnames[p]=[args][i]
                else:
                    self.forumnames[p].append(args)
                i=i+1


    def __init__questions(self):
        args=get_questions_io()
        self.questions=[[None]]
        i=0
        size=100
        size1=2000


    def __init__add_answer_to_question(self,forum_name,question_in_forum,answer):
       index=self.hash_function(forum_name,100)
       print index,self.forumnames[index]
       print forum_name
       print self.forumnames[index] == forum_name
       print type(self.forumnames[index])
       print type(forum_name)
       if forum_name is self.forumnames[index]:

           questions_list=retrieve_getQue(forum_name)
           for question in question:
               if question == question_in_forum:
                   msg=add_ans_toQue_forum(forum_name,question_in_forum,answer)
                   return msg
           return "Question does not exist"
       return "Forum does not exist"



