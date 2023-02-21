from sklearn.cluster import SpectralClustering


def solve(affinity, n, m, k, epsilon, time):
    sc = SpectralClustering(n_clusters=k, affinity='precomputed')
    partitions = sc.fit_predict(affinity)
    ans = 0
    for i in range(n):
        for j in range(i):
            if partitions[i] != partitions[j]:
                ans += affinity[i][j]
    return ans
