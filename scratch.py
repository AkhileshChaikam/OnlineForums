import threading


# creating a thread.
import thread


class Worker(threading.Thread):
    def __init__(self,x):
        self.x = x
        threading.Thread.__init__(self)
    def run (self):
        i = 0
        while i < 10:
            print threading.current_thread().name, "[", str(self.x), "]"


def thread_demo():
    for x in xrange(10):
        worker_thread = Worker(x)
        worker_thread.start()


count = 0

def increment():
    global count
    count += 1


# sample race condition, what locks will u you use to make this thread safe?
class mythread(threading.Thread):
    def __init__(self,func,bal,l):
        threading.Thread.__init__(self)
        self.fun=func
        self.bal=bal
        self.lock=l
    def run(self):
        self.lock.acquire()
        self.fun(self.bal)
        self.lock.release()

class Account(object):
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance

    def set_balance(self, value):
        self.balance = value

    def debit(self, value):
        balance = self.get_balance()
        time.sleep(5)
        balance -= value
        self.set_balance(balance)
        print "after debit{0}".format(self.get_balance())

    def credit(self, value):
        balance = self.get_balance()
        time.sleep(5)
        balance += value
        self.set_balance(balance)
        print "after credit{0}".format(self.get_balance())

import urllib2, json, time

#urls = ['http://www.google.com', 'http://www.yahoo.com', 'http://www.stackoverflow.com']
urls = ['http://www.google.com', 'http://www.google.com', 'http://www.google.com']
results = []

start_time = None

def fetch(url):
    response = urllib2.urlopen(url)
    result = response.read()
    print 'Finished fetching {0} url at time {1}'.format(url, time.time() - start_time)


def sequential_fetch():
    for url in urls:
        fetch(url)

def parallel_fetch():
    for url in urls:
        t = threading.Thread(None, target = fetch, args =(url,))
        t.start()

def main():
    # thread_demo()

    global start_time
    start_time = time.time()
    sequential_fetch()
    #
    start_time = time.time()
    parallel_fetch()




if __name__ == "__main__":
    a=Account()
    a.set_balance(10000)
    l=threading.Lock()
    t1=mythread(a.credit,2000,l)
    t2=mythread(a.debit,3000,l)
    t1.start()
    t2.start()
    t1.join()
    t2.join()