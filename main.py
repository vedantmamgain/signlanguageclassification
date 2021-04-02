from pandas import read_csv
import numpy as np


def load_file(filepath):
    dataframe = read_csv(filepath, header=None, delimiter=',')
    return dataframe.values


def load_subject(sub_idx, sign, start, end):
    filepath = str("Dataset/20_sign_language/" + "S" + str(sub_idx) + "_RA" + str(sign) + ".csv")
    dataframe = read_csv(filepath, header=None, delimiter=',', skiprows=start, nrows=end)
    return dataframe.values


def load_rows(start, end):
    arr = []
    arr.append(load_subject(1, 61, start, end))
    print(arr)


def load_time(sub_idx, sign):
    return load_file(
        str("Dataset/20_sign_language/Start_end_point/ipt_" + "S" + str(sub_idx) + "_RA" + str(sign) + ".csv"))


def main(sign):
    data = []
    for x in range(1, 5):
        data.append(load_time(x, sign))
    arr = np.array(data)
    load_rows(10,20)
    # print all the values of the start and end of repretitions person wise
	# for k in range(0, 39, 2):
    # start = arr[0, k, 0], end = arr[0,k + 1, 0]
    # load_rows(start,end,fin)
    # print(arr[0, k, 0],arr[0, k+1, 0])


main(61)
