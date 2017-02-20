import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
import glob, os
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt


def example_one():

    path = "D:\\PYTHON\\OZ_2\\Activity Recognition from Single Chest-Mounted Accelerometer\\Activity Recognition from Single Chest-Mounted Accelerometer\\"
    array = []

    for file in os.listdir(path):
        if (file.endswith(".csv")):
            print(file)
            array.append(pd.read_csv(str(path)+str(file)))

    print("Loaded all .csv files")
    frame = pd.concat(array)

    frame.to_csv("all.csv", sep=',')

def read_all_data():
    frame = pd.read_csv("all.csv")
    print("Data was loaded")
    pd.head(frame)
    return frame


def main():
    print("Starting")

    #example_one()
    frame = read_all_data()




if __name__ == '__main__':
    main()

