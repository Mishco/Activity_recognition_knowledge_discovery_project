# preprocessing
import pandas as pd
import sys

def main():
    """
    Metoda na pouzitie sliding window
    """

    all_csv = pd.read_csv("all2.csv")
    #print(all_csv)

    start = 0
    end = 99

    slidedataframe = pd.DataFrame()
    iteration=1
    mycolumns=[]
    while (all_csv.size-1 > end):
        tmp = all_csv.ix[start:end,1:4]
        movement = all_csv.ix[end,4]
        userid = all_csv.ix[end,5]
        tmp = tmp.stack().to_frame().T

        if iteration == 1:
            mycolumns=['{}_{}'.format(*c) for c in tmp.columns]
            iteration=2
        tmp.columns = mycolumns
        # print (tmp.columns)
        tmp['movement'] = movement
        tmp['userid'] = userid

        slidedataframe = slidedataframe.append(tmp)
        start += 1
        end += 1
        if (end == 100):
        #if (end > 100 == 0):
            # print(end)
            print(slidedataframe)
            break

    # save to csv


    #print(slidedataframe.shape)



if __name__ == '__main__':
    main()