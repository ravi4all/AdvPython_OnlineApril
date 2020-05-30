import threading
import time

def job():
    print("Job Started by {}".format(threading.current_thread().getName()))
    time.sleep(2)
    for i in range(1000):
        for j in range(1000):
            k = i + j
    print("Job Ended by {}".format(threading.current_thread().getName()))

print(threading.current_thread().getName())

for i in range(5):
    t = threading.Thread(target=job, name = 'Thread_{}'.format(i))
    t.start()
