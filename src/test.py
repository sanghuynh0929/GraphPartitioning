'''
10vers, 25 edges, 2 clusters, alpha = 2
20vers, 50 edges, 2 clusters, alpha = 2
20vers, 50 edges, 4 clusters, alpha = 2
50vers, 125 edges, 2 clusters, alpha = 2
50vers, 125 edges, 4 clusters, alpha = 4
100vers, 250 edges, 2 clusters, alpha = 2
100vers, 250 edges, 8 clusters, alpha = 8
1000vers, 2500 edges, 2 clusters, alpha = 4
1000vers, 2500 edges, 4 clusters, alpha = 8
1000vers, 2500 edges, 16 clusters, alpha = 10
'''
import backtracking_alpha, backtracking_epsilon, \
    CP_alpha, IP_alpha, CP_epsilon, IP_epsilon, \
    spectral_sklearn, greedy_KL

def set10():
    # test against backtracking alpha, CP_alpha, IP_alpha,
    # test against backtracking epsilon, CP_epsilon, IP_epsilon, spectral_sklearn, greedy
    for i in range(1, 21):
        with open(f"../data/20ver/test{i}.txt") as f:
            print(f"TEST {i}:")
            affinity = list()
            n = 20
            m = 50
            k = 2
            alpha = 0
            epsilon = 0.5
            for line in f:
                x = [int(x) for x in line.split()]
                affinity.append(x)
            print(backtracking_alpha.solve(affinity, n, m, k, alpha, 10000))
            print(CP_alpha.solve(affinity, n, m, k, alpha, 10000))
            print(IP_alpha.solve(affinity, n, m, k, alpha, 10000))
            print(backtracking_epsilon.solve(affinity, n, m, k, epsilon, 10000))
            print(CP_epsilon.solve(affinity, n, m, k, epsilon, 10000))
            print(IP_epsilon.solve(affinity, n, m, k, epsilon, 10000))
            print(spectral_sklearn.solve(affinity, n, m, k, epsilon, 10000))
            print(greedy_KL.solve(affinity, n, m, k, epsilon, 10000))
            print()

def set20():
    pass

def set50():
    pass

def set100():
    pass

def set1000():
    pass


if __name__ == '__main__':
    set10()
    set20()
    set50()
    set100()
    set1000()