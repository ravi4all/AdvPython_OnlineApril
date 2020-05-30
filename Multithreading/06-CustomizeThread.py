import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s')

class MyThread(threading.Thread):

    def __init__(self,group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('Running with %s and %s'%(self.args, self.kwargs))

for i in range(5):
    obj = MyThread(args=(i,), kwargs={'a':'A', 'b':'B'})
    obj.start()