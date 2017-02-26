import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
import glob, os
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt


def example_one():

    path = "Activity Recognition from Single Chest-Mounted Accelerometer\\Activity Recognition from Single Chest-Mounted Accelerometer\\"
    array = []

    for file in os.listdir(path):
        if (file.endswith(".csv")):
            print(file)
            array.append(pd.read_csv(str(path)+str(file)))

    print("Loaded all .csv files")
    frame = pd.concat(array)
    
    # frame['id'] = frame['id'].apply(np.int64) #takto sa meni dtype columnu
    # frame.index = frame.index.map(np.int64) #takto sa meni dtype indexu

    frame = frame.drop('id', axis=1)

    frame.to_csv("all.csv", sep=',')

def read_all_data():
    frame = pd.read_csv("all.csv")
    frame.set_index('id', inplace=True) #aby pandas vedelo ze index ma brat z id
    print("Data was loaded")
    frame.head()

    return frame


def main():
    print("Starting")
    # example_one()
    frame = read_all_data()




if __name__ == '__main__':
    main()

