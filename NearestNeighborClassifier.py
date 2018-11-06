import numpy as np

def NearestNeighborClassifier(data, centroid1Points, centroid2Points):
    l = []
    for i in range(data.shape[1]):
        distanceC2 = []
        distanceC1 = []
        for j in range(centroid1Points.shape[1]):
            distanceC1.append(np.linalg.norm(data[:, i] - centroid1Points[:, j]))

        for j in range(centroid2Points.shape[1]):
            distanceC2.append(np.linalg.norm(data[:, i] - centroid2Points[:, j]))
        print(min(distanceC1))
        print(min(distanceC2))
        if min(distanceC1) > min(distanceC2):
            l.append('l2')
        else:
            l.append('l1')

    data = {'labels': l,
            'distanceC1': distanceC1,
            'distanceC2': distanceC2}
    return data