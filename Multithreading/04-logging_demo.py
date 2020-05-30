import logging
import time, threading

# Logging levels
# CRITICAL
# ERROR
# WARNING
# INFO
# DEBUG
# NOTSET

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s')

def job():
    logging.debug('Starting...')
    time.sleep(2)
    logging.debug('Exiting...')

for i in range(3):
    th = threading.Thread(target=job)
    th.start()
