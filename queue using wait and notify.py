__author__ = 'Shrikita'
import threading
import time
class deque(threading.Thread):
    def __init__(self,func):
        threading.Thread.__init__(self)
        self.delete=func
    def run(self):
        self.delete()
        self.delete()
        self.delete()
        self.delete()
        self.delete()
        self.delete()
        self.delete()
        self.delete()

class enque(threading.Thread):
    def __init__(self,func):
        threading.Thread.__init__(self)
        self.add=func
    def run(self):
        self.add(1)
        self.add(2)
        self.add(3)
        self.add(4)
        self.add(5)
        self.add(6)
        self.add(7)
        self.add(8)
class queue:
    def __init__(self,max):
        self.que=[None]*max
        self.head=self.tail=-1
        self.max=max
        self.lock=threading.Condition()
    def length(self):
        if(self.head==-1):
            return 0
        else:
            i=self.tail
            l=1
            while(self.head!=i):
                i=(i+1)%self.max
                l=l+1
            return l
    def enqueue(self,e):
        self.lock.acquire()
        if(self.length()==self.max):
            self.lock.wait()
        if(self.head==-1):
            self.head=self.tail=0
        else:
            self.head=(self.head+1)%self.max
        self.que[self.head]=e
        print self.que
        if(len(self.que)==1):
            self.lock.notify()
        self.lock.release()
    def dequeue(self):
        self.lock.acquire()
        if(self.length()==0):
            self.lock.wait()
        self.que[self.tail]=None
        if(self.head==self.tail):
            self.head=self.tail=-1
        else:
            self.tail=(self.tail+1)%self.max
        print self.que
        if(len(self.que)==self.max-1):
            self.lock.notify()
        self.lock.release()

t=queue(3)
t1=enque(t.enqueue)
t2=deque(t.dequeue)
t1.start()
t2.start()
t1.join()
t2.join()