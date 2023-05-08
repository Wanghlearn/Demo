from file_read import data_process as dp
import numpy as np
from scipy.spatial.distance import cdist


def DynamicTimeWarping(err_seq, cmp_seq):
    """ 计算两序列的DTW距离

    err_seq: 已知异常序列
    cmp_seq: 待检测序列
    :return: DTW距离
    """

    n, m = err_seq.shape[0], cmp_seq.shape[0]
    dist_matrix = cdist(err_seq, cmp_seq, metric='euclidean')
    cost_matrix = np.full((n, m), -1.0)

    # 初始化
    cost_matrix[0][0] = dist_matrix[0][0]
    for i in range(n):
        cost_matrix[i][0] = cost_matrix[i - 1][0] + dist_matrix[i][0]
    for i in range(m):
        cost_matrix[0][i] = cost_matrix[0][i - 1] + dist_matrix[0][i]
    for i in range(1, n):
        for j in range(1, m):
            cost_matrix[i][j] = min(cost_matrix[i - 1][j],
                                    cost_matrix[i - 1][j - 1],
                                    cost_matrix[i][j - 1]) + dist_matrix[i][j]

    return cost_matrix[n - 1][m - 1]


def seqSort():
    """调用DTW函数对序列按距离升序排序

    :return: 升序排序的字典
    """

    dataset = dp.read()
    dist_dict = {}
    for i in range(1, 21):
        dist_dict[DynamicTimeWarping(dataset[0], dataset[i])] = i
    new_dict = sorted(dist_dict.items())
    return new_dict,dataset

