import threading
import time

class ThreadSafety():

    def __init__(self,bal):
        self.bal = bal

    def balance(self, amount):
        try:
            print("Hello", threading.current_thread().getName(),"balance is", self.bal)
            time.sleep(2)
            if self.bal > amount:
                self.bal = self.bal - amount
                print(threading.current_thread().getName(), "Your Remaning balance :",self.bal)
            else:
                print("Can't withdraw for {}".format(threading.current_thread().getName()))
        except Exception as ex:
            print(ex)

        print("Balance after transaction by : ",threading.current_thread().getName(),"is",self.bal)

obj = ThreadSafety(10000)

t1 = threading.Thread(target=obj.balance, args=(5000,), name = 'Ram')
t2 = threading.Thread(target=obj.balance, args=(10000,), name = 'Shyam')

t1.start()
t2.start()