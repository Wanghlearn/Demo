import pandas as pd
from sklearn import preprocessing


def read():
    """ 读取csv文件并截取异常数据，进行标准化

    :return: 已处理好的数据集
    """

    file_path = "AIBMA-ES-CLUSTER-20230423/"
    file_suffix = ".csv"

    for i in range(21):
        data_csv = pd.read_csv(file_path + str(i) + file_suffix)

        data_csv_value = data_csv['value']
        data_csv_time = data_csv['timestamp']

        if i == 0:
            data_csv_value = data_csv_value[16:77]
            data_csv_time = data_csv_time[16:77]
        else:
            data_csv_value = data_csv_value[14:80]
            data_csv_time = data_csv_time[14:80]

        dataframe_csv = pd.DataFrame({'timestamp': data_csv_time, 'value': data_csv_value})
        dataframe_csv.to_csv("data_set/data_" + str(i) + ".csv", index=False, sep=',')

    dataset = []
    for i in range(21):
        data = pd.read_csv('data_set/data_' + str(i) + '.csv', delimiter=",")
        data = data.values
        # normalization
        min_max_scaler = preprocessing.MinMaxScaler()
        data = min_max_scaler.fit_transform(data)
        dataset.append(data)

    return dataset

