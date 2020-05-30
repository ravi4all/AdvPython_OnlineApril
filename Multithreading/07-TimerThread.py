import threading
import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s')

def delayed():
    logging.debug('Running...')

t1 = threading.Timer(3,delayed)
t1.setName('Thread-1')

t2 = threading.Timer(1, delayed)
t2.setName('Thread-2')

logging.debug('Starting timer threads...')
t1.start()
t2.start()

time.sleep(5)
logging.debug('Cancelling {}'.format(t2.getName()))
t2.cancel()
logging.debug('DONE...')