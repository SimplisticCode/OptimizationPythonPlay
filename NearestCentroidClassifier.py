import numpy as np


def NearestCentroid(data, centroid1, centroid2):
    l = []
    distanceC1 = []
    distanceC2 = []
    for i in range(data.shape[1]):
        distanceC1.append(np.linalg.norm(data[:, i] - centroid1))
        distanceC2.append(np.linalg.norm(data[:, i] - centroid2))
        if distanceC1[i] > distanceC2[i]:
            l.append('l2')
        else:
            l.append('l1')

    data = {'labels': l,
            'distanceC1': distanceC1,
            'distanceC2': distanceC2}
    return data
