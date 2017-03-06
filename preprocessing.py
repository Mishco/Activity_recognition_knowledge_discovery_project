import pandas as pd
import sys

def main():
    all_csv = pd.read_csv("all.csv")
    #print(all_csv)

    start = 0
    end = 99

    slidedataframe = pd.DataFrame()

    while (all_csv.size-1 > end):
        tmp = all_csv.ix[start:end]
        slidedataframe.append(tmp)
        start += 1
        end += 1
        #sys.stdout.write('.')
        if (end % 1000 == 0):
            print(end)

    print(slidedataframe.shape)








if __name__ == '__main__':
    main()