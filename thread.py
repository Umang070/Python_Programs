#THREAD MEANS MANY PROCESS RUNNING SIMULTANEOUSLY

from time import sleep
from threading import *

class Umang(Thread):
        def run(self):
            for i in range(5):
                    print("Welcome")
                    sleep(1)
class Patel(Thread):
        def run(self):
            for i in range(5):
                    print("Coder")
                    sleep(1)

u1 = Umang()
p1 = Patel()

u1.start()  #u1 thred
sleep(0.2)  #for remove collison........
p1.start()  #p1 thred

u1.join()
p1.join() 

print("BYE")        #It's prinnt by main thread...so it prinnt btw 