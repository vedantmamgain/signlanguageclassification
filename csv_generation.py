from pandas import read_csv
import numpy as np
import pandas as pd
import csv

def load_file(filepath):
    dataframe = read_csv(filepath, header=None, delimiter=',')
    return dataframe.values


def load_subject(sub_idx, sign, start, end, idx1, idx2):
    start -= 1
    end -= 1
    filepath = str("Dataset/20_sign_language/" + "S" + str(sub_idx) + "_RA" + str(sign) + ".csv")
    # fix why n rows has an offset of 8
    dataframe = read_csv(filepath, header=None, delimiter=',', skiprows=start, nrows=end - 8,
                         usecols=[*range(idx1, idx2)])
    #print(dataframe.values)
    return dataframe.values


def load_rows(start, end, sign, sub_idx):
    arr = []
    arr.append(sign)
    # for emg right  3->5
    arr.append(load_subject(sub_idx, sign, start[0], end[0], 3, 5))
    # for accelo right  9->17
    arr.append(load_subject(sub_idx, sign, start[1], end[1], 9, 17))
    # for gyro right 27->35
    arr.append(load_subject(sub_idx, sign, start[2], end[2], 27, 35))
    # for emg left  6->8
    arr.append(load_subject(sub_idx, sign, start[3], end[3], 6, 8))
    # for accelo left 18->26
    arr.append(load_subject(sub_idx, sign, start[4], end[4], 18, 26))
    # for gyro left  36->44
    arr.append(load_subject(sub_idx, sign, start[5], end[5], 36, 44))
    #print(arr)
    return np.array(arr, dtype=object)


def load_time(sub_idx, sign):
    return load_file(
        str("Dataset/20_sign_language/Start_end_point/ipt_" + "S" + str(sub_idx) + "_RA" + str(sign) + ".csv"))

cols=['Sign', 'Code', 'Age', 'Weight','Name', 'Code', 'Age']

final = []
def main(sign):
    data = []
    for x in range(1, 5):
        data.append(load_time(x, sign))
    arr = np.array(data)
    # print all the values of the start and end of repetitions person wise
    for p in range(1, 5):
        for k in range(0, 39, 2):
            start = arr[p - 1, k]
            end = arr[p - 1, k + 1]
            final.append(np.array(load_rows(start, end, sign, p)))



for p in range(61,81):
  main(p)
df=pd.DataFrame(final)
df.dropna(
        axis=0,
        how='any',
        thresh=None,
        subset=None,
        inplace=True
    )
df.columns = cols
df.to_csv('final.csv')
