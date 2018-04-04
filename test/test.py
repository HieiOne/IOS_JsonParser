import time
from threading import Thread

def noInterrupt():
    for i in range(4):
        print(i)
        time.sleep(1)

a = Thread(target=noInterrupt)
a.start()
a.join()
print("done")