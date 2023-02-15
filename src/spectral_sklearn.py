from sklearn.cluster import SpectralClustering


def solve(affinity, n, m, k, epsilon, time):
    sc = SpectralClustering(n_clusters=k, affinity='precomputed')
    partitions = sc.fit_predict(affinity)
    return partitions
