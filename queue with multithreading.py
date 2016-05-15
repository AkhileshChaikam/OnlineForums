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
        self.add([1,2])
        self.add([3,4])
        self.add([5,6])
        self.add([7,8])
        self.add([9,10])
        self.add([11,12])
        self.add([13,14])
        self.add([15,16])
        self.add([17,18])
        self.add([19,20])
        self.add([21,22])
        self.add([23,24])
        self.add([25,26])
        self.add([27,28])
        self.add([29,30])
        self.add([31,32])
class queue:
    def __init__(self,max,min):
        self.que=[None]*max
        self.head=self.tail=-1
        self.max=max#maximum size of the queue
        self.min=min#no of items that can be added at a time
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
        if(self.length()>self.max-self.min):
            self.lock.wait()
        if(self.head==-1):
            self.head=self.tail=0
        else:
            self.head=(self.head+1)%self.max
        self.que[self.head]=e[0]
        self.head=(self.head+1)%self.max
        self.que[self.head]=e[1]
        print self.que
        if(len(self.que)>0):
            self.lock.notifyAll()
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
        if(len(self.que)<=self.max-self.min):
            self.lock.notifyAll()
        self.lock.release()

t=queue(5,2)
t1=enque(t.enqueue)
t2=deque(t.dequeue)
t3=deque(t.dequeue)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()