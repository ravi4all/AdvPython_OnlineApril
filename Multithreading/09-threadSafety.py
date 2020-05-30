import threading
import time

class ThreadSafety():

    def __init__(self,bal):
        self.bal = bal

    def balance(self, amount):
        lock.acquire()
        try:
            print("Hello", threading.current_thread().getName(),"balance is", self.bal)
            print("Lock acquired by {}".format(threading.current_thread().getName()))
            time.sleep(2)
            if self.bal > amount:
                self.bal = self.bal - amount
                print(threading.current_thread().getName(), "Your Remaning balance :",self.bal)
            else:
                print("Can't withdraw for {}".format(threading.current_thread().getName()))
        except Exception as ex:
            print(ex)

        print("Balance after transaction by : ",threading.current_thread().getName(),"is",self.bal)
        lock.release()
        print("Lock released by {}".format(threading.current_thread().getName()))

obj = ThreadSafety(10000)
lock = threading.Lock()
t1 = threading.Thread(target=obj.balance, args=(5000,), name = 'Ram')
t2 = threading.Thread(target=obj.balance, args=(9000,), name = 'Shyam')

t1.start()
t2.start()