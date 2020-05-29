import threading

def job_1():
    print("Job_1 Start")
    for i in range(10000):
        for j in range(10000):
            k = i + j
    print("Job_1 Done")

def job_2():
    print("Job_2 Started")
    for i in range(100):
        for j in range(10):
            k = i + j
    print("Job_2 Done")

worker_1 = threading.Thread(target=job_1)
worker_2 = threading.Thread(target=job_2)

worker_1.start()
worker_2.start()
