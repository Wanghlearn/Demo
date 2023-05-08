from dtw import seqSort
import pandas as pd
from sklearn import preprocessing


def getAns():
    """返回答案

    :return: 按相似度返回序号、距离、数据
    """

    new_dict, dataset_all = seqSort()
    dataset = []
    i = 0
    min_max_scaler = preprocessing.MinMaxScaler()
    for k, v in new_dict:
        if i < 5:
            data = pd.read_csv('data_set/data_' + str(v) + '.csv', delimiter=",")
            data = data.values
            data = min_max_scaler.fit_transform(data)
            dataset.append(data.tolist())
        else:
            break
        i += 1

    data = pd.read_csv('data_set/data_0.csv', delimiter=",")
    data = min_max_scaler.fit_transform(data)
    dataset.append(data.tolist())
    print(dataset)

    return new_dict, dataset

