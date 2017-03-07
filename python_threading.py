import threading

class SummingThread(threading.Thread):
    """Studijna trieda na vlakna"""
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             self.total+=i*2


class SlidingWindow(threading.Thread):
    def __init__(self,low, high):
        super(SlidingWindow, self).__init__()
        self.low=low    # rozsah intervalu od
        self.high=high  # do

    def run(self):
        # cyklus v rozsahu
        for i in range(self.low, self.high):
            self.res = self.low + self.high



thread1 = SlidingWindow(0,99)
thread2 = SlidingWindow(100,199)

thread1.start()
thread2.start()

print(thread1.res)
print(thread2.res)

# thread1 = SummingThread(0,50000000)
# thread2 = SummingThread(500000,100000000)
#
# thread1.start() # This actually causes the thread to run
# thread2.start()
#
# thread1.join()  # This waits until the thread has completed
# thread2.join()
# # At this point, both threads have completed
# result = thread1.total + thread2.total
# print (result)