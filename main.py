from pandas import read_csv
import numpy as np
import pandas as pd
def load_file(filepath):
    dataframe = read_csv(filepath, header=None, delimiter=',')
    return dataframe.values


def load_subject(sub_idx, sign, start, end):
    start -= 1
    end -= 1
    filepath = str("Dataset/20_sign_language/" + "S" + str(sub_idx) + "_RA" + str(sign) + ".csv")
    # fix why n rows has an offset of 8
    dataframe = read_csv(filepath, header=None, delimiter=',', skiprows=start, nrows=end - 8)
    return dataframe.values


def load_rows(start, end, sign,sub_idx):
    arr = []
    arr.append(load_subject(sub_idx, sign, start, end))
    #print(arr)
    return arr


def load_time(sub_idx, sign):
    return load_file(
        str("Dataset/20_sign_language/Start_end_point/ipt_" + "S" + str(sub_idx) + "_RA" + str(sign) + ".csv"))


def main(sign):
    data = []
    for x in range(1, 5):
        data.append(load_time(x, sign))
    arr = np.array(data)
    final = []
    # print all the values of the start and end of repretitions person wise
    for p in range(1,5):
        for k in range(0, 39, 2):
            start = arr[p-1, k, 0]
            end = arr[p-1, k + 1, 0]
            final.append(load_rows(start, end, sign,p))
            # print(arr[0, k, 0],arr[0, k+1, 0])
    check =  pd.DataFrame(final)
    check.to_csv('finalCheck.csv')
    #print(final)

main(61)
