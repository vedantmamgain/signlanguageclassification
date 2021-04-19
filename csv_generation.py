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
    filepath = str("/content/gdrive/My Drive/Dataset/20_sign_language/" + "S" + str(sub_idx) + "_RA" + str(sign) + ".csv")
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
        str("/content/gdrive/My Drive/Dataset/20_sign_language/Start_end_point/ipt_" + "S" + str(sub_idx) + "_RA" + str(sign) + ".csv"))

cols=['Sign', 'EMG-R', 'ACC-R', 'GYRO-R','EMG-L', 'ACC-L', 'GYRO-L']

main_cols=['Sign', 'EMG-R-1','EMG-R-2','EMG-R-3',
      'ACC-Rx-1','ACC-Ry-1','ACC-Rz-1',
      'ACC-Rx-2','ACC-Ry-2','ACC-Rz-3',
      'ACC-Rx-3','ACC-Ry-3','ACC-Rz-3',
      'GYRO-Rx-1','GYRO-Ry-1','GYRO-Rz-1',
      'GYRO-Rx-2','GYRO-Ry-2','GYRO-Rz-3',
      'GYRO-Rx-3','GYRO-Ry-3','GYRO-Rz-3',
      'EMG-L-1','EMG-L-2','EMG-L-3',
      'ACC-Lx-1','ACC-Ly-1','ACC-Lz-1',
      'ACC-Lx-2','ACC-Ly-2','ACC-Lz-3',
      'ACC-Lx-3','ACC-Ly-3','ACC-Lz-3',
      'GYRO-Lx-1','GYRO-Ly-1','GYRO-Lz-1',
      'GYRO-Lx-2','GYRO-Ly-2','GYRO-Lz-3',
      'GYRO-Lx-3','GYRO-Ly-3','GYRO-Lz-3',]

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



for p in range(61,80):
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