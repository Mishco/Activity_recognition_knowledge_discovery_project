import threading
import pandas as pd
import numpy as np


all_csv = pd.read_csv("all2.csv",
                      dtype={'x': np.int16, 'y': np.int16, 'z': np.int16, 'movement': np.int8, 'user': np.int8})

class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             self.total+=i*2



class SlidingWindow(threading.Thread):
    def __init__(self,low, high, name):
        super(SlidingWindow, self).__init__()
        self.low=low    # rozsah intervalu od
        self.high=high  # do
        self.name=name  # meno suboru

    def run(self):
        # cyklus v rozsahu
        # for i in range(self.low, self.high, self.name):
        #     self.res = self.low + self.high
        start = self.low
        end = self.high
        slidedataframe = pd.DataFrame()
        iteration = 1
        mycolumns = []
        prev_movement = all_csv.ix[end, 4]
        prev_userid = all_csv.ix[end, 5]

        for i in range(start, end):
            #while (all_csv.size - 1 > end):
            movement = all_csv.ix[end, 4]
            userid = all_csv.ix[end, 5]
            if (prev_movement != movement) or (prev_userid != userid):
                start = end
                end = start + 99
                prev_movement = movement
                prev_userid = userid
                continue
            tmp = all_csv.ix[start:end, 1:4]
            tmp = tmp.stack().to_frame().T
            prev_movement = movement
            prev_userid = userid

            if iteration == 1:
                mycolumns = ['{}_{}'.format(*c) for c in tmp.columns]
                iteration = 2
            tmp.columns = mycolumns
            # print (tmp.columns)
            tmp['movement'] = movement
            tmp['user'] = userid
            tmp[['movement', 'user']] = tmp[['movement', 'user']].astype(np.int8)

            slidedataframe = slidedataframe.append(tmp)
            start += 1
            end += 1
            if (end % 1000 == 0):
                print(end)

        # save to csv
        slidedataframe.to_csv(self.name, sep=',')

thread1 = SlidingWindow(0,99, "sliding1.csv")
thread2 = SlidingWindow(100,199, "sliding2.csv")

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