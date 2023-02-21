'''
10vers, 25 edges, 2 clusters, alpha = 2
20vers, 50 edges, 2 clusters, alpha = 2
50vers, 125 edges, 2 clusters, alpha = 2
50vers, 750 edges, 2 clusters, alpha = 2


100vers, 250 edges, 2 clusters, alpha = 2
100vers, 250 edges, 4 clusters, alpha = 2
100vers, 2250 edges, 2 clusters, alpha = 2
100vers, 2250 edges, 4 clusters, alpha = 2
1000vers, 2500 edges, 2 clusters, alpha = 4
1000vers, 2500 edges, 8 clusters, alpha = 4
1000vers, 20000 edges, 2 clusters, alpha = 4
1000vers, 20000 edges, 8 clusters, alpha = 4

'''

import time, contextlib
import backtracking_alpha, backtracking_epsilon, \
    CP_alpha, IP_alpha, CP_epsilon, IP_epsilon, \
    spectral_sklearn, greedy_KL, greedy

def set10():
    # test against backtracking alpha, CP_alpha, IP_alpha,
    # test against backtracking epsilon, CP_epsilon, IP_epsilon, spectral_sklearn, greedy
    for i in range(1, 21):
        with open(f"../data/10ver/test{i}.txt") as f:
            print(f"TEST {i}:")
            affinity = list()
            n = 10
            m = 25
            k = 2
            alpha = 0
            epsilon = 0.2
            for line in f:
                x = [int(x) for x in line.split()]
                affinity.append(x)

            st = time.time()
            res = backtracking_alpha.solve(affinity, n, m, k, alpha, 10000)
            fn = time.time()
            print("Backtracking(alpha)", res, round(fn - st, 4))

            st = time.time()
            res = CP_alpha.solve(affinity, n, m, k, alpha, 10000)
            fn = time.time()
            print("CP(alpha)", res, round(fn - st, 4))

            st = time.time()
            res = IP_alpha.solve(affinity, n, m, k, alpha, 10000)
            fn = time.time()
            print("IP(alpha)", res, round(fn - st, 4))

            st = time.time()
            res = backtracking_epsilon.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("Backtracking(eps)", res, round(fn - st, 4))

            st = time.time()
            res = CP_epsilon.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("CP(eps)", res, round(fn - st, 4))

            st = time.time()
            res = IP_epsilon.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("IP(eps)", res, round(fn - st, 4))

            st = time.time()
            res = spectral_sklearn.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("Spectral", res, round(fn - st, 4))

            st = time.time()
            res = greedy.solve(affinity, n, m, k, epsilon, 500)
            fn = time.time()
            print("Greedy(500)", res, round(fn - st, 4))

            st = time.time()
            res = greedy.solve(affinity, n, m, k, epsilon, 1000)
            fn = time.time()
            print("Greedy(1000)", res, round(fn - st, 4))

            st = time.time()
            res = greedy_KL.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("GreedyKL", res, round(fn - st, 4))

def set20():
    for i in range(1, 20):
        with open(f"../data/20ver/test{i}.txt") as f:
            print(f"TEST {i}:")
            affinity = list()
            n = 20
            m = 50
            k = 2
            alpha = 0
            epsilon = 0.2
            for line in f:
                x = [int(x) for x in line.split()]
                affinity.append(x)
            st = time.time()
            res = backtracking_alpha.solve(affinity, n, m, k, alpha, 10000)
            fn = time.time()
            print("Backtracking(alpha)", res, round(fn - st, 4))

            st = time.time()
            res = CP_alpha.solve(affinity, n, m, k, alpha, 10000)
            fn = time.time()
            print("CP(alpha)", res, round(fn - st, 4))

            st = time.time()
            res = IP_alpha.solve(affinity, n, m, k, alpha, 10000)
            fn = time.time()
            print("IP(alpha)", res, round(fn - st, 4))

            st = time.time()
            res = backtracking_epsilon.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("Backtracking(eps)", res, round(fn - st, 4))

            st = time.time()
            res = CP_epsilon.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("CP(eps)", res, round(fn - st, 4))

            st = time.time()
            res = IP_epsilon.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("IP(eps)", res, round(fn - st, 4))

            st = time.time()
            res = spectral_sklearn.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("Spectral", res, round(fn - st, 4))

            st = time.time()
            res = greedy.solve(affinity, n, m, k, epsilon, 500)
            fn = time.time()
            print("Greedy(500)", res, round(fn - st, 4))

            st = time.time()
            res = greedy.solve(affinity, n, m, k, epsilon, 1000)
            fn = time.time()
            print("Greedy(1000)", res, round(fn - st, 4))

            st = time.time()
            res = greedy_KL.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("GreedyKL", res, round(fn - st, 4))

def set50sparse():
    for i in range(1, 21):
        with open(f"../data/50ver_sparser/test{i}.txt") as f:
            print(f"TEST {i}:")
            affinity = list()
            n = 50
            m = 125
            k = 2
            alpha = 0
            epsilon = 0.1
            for line in f:
                x = [int(x) for x in line.split()]
                affinity.append(x)

            st = time.time()
            res = CP_alpha.solve(affinity, n, m, k, alpha, 10000)
            fn = time.time()
            print("CP(alpha)", res, round(fn - st, 4))

            st = time.time()
            res = IP_alpha.solve(affinity, n, m, k, alpha, 10000)
            fn = time.time()
            print("IP(alpha)", res, round(fn - st, 4))

            st = time.time()
            res = CP_epsilon.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("CP(eps)", res, round(fn - st, 4))

            st = time.time()
            res = IP_epsilon.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("IP(eps)", res, round(fn - st, 4))

            st = time.time()
            res = spectral_sklearn.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("Spectral", res, round(fn - st, 4))

            st = time.time()
            res = greedy.solve(affinity, n, m, k, epsilon, 500)
            fn = time.time()
            print("Greedy(500)", res, round(fn - st, 4))

            st = time.time()
            res = greedy.solve(affinity, n, m, k, epsilon, 1000)
            fn = time.time()
            print("Greedy(1000)", res, round(fn - st, 4))

            st = time.time()
            res = greedy_KL.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("GreedyKL", res, round(fn - st, 4))

def set50dense():
    for i in range(1, 21):
        with open(f"../data/50ver_denser/test{i}.txt") as f:
            print(f"TEST {i}:")
            affinity = list()
            n = 50
            m = 125
            k = 2
            alpha = 0
            epsilon = 0.1
            for line in f:
                x = [int(x) for x in line.split()]
                affinity.append(x)

            st = time.time()
            res = CP_alpha.solve(affinity, n, m, k, alpha, 10000)
            fn = time.time()
            print("CP(alpha)", res, round(fn - st, 4))

            st = time.time()
            res = IP_alpha.solve(affinity, n, m, k, alpha, 10000)
            fn = time.time()
            print("IP(alpha)", res, round(fn - st, 4))

            st = time.time()
            res = CP_epsilon.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("CP(eps)", res, round(fn - st, 4))

            st = time.time()
            res = IP_epsilon.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("IP(eps)", res, round(fn - st, 4))

            st = time.time()
            res = spectral_sklearn.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("Spectral", res, round(fn - st, 4))

            st = time.time()
            res = greedy.solve(affinity, n, m, k, epsilon, 500)
            fn = time.time()
            print("Greedy(500)", res, round(fn - st, 4))

            st = time.time()
            res = greedy.solve(affinity, n, m, k, epsilon, 1000)
            fn = time.time()
            print("Greedy(1000)", res, round(fn - st, 4))

            st = time.time()
            res = greedy_KL.solve(affinity, n, m, k, epsilon, 10000)
            fn = time.time()
            print("GreedyKL", res, round(fn - st, 4))

def set100sparse():
    for i in range(1, 21):
        with open(f"../data/100ver_sparser/test{i}.txt") as f:
            print(f"TEST {i}:")
            affinity = list()
            n = 50
            m = 125
            k = 2
            alpha = 0
            epsilon = 0.1
            for line in f:
                x = [int(x) for x in line.split()]
                affinity.append(x)
            print(spectral_sklearn.solve(affinity, n, m, k, epsilon, 10000))
            print(greedy.solve(affinity, n,m,k,epsilon,500))
            print(greedy.solve(affinity, n,m,k,epsilon,1000))
            print(greedy_KL.solve(affinity, n, m, k, epsilon, 10000))
            print()

def set100dense():
    for i in range(1, 21):
        with open(f"../data/100ver_denser/test{i}.txt") as f:
            print(f"TEST {i}:")
            affinity = list()
            n = 50
            m = 125
            k = 2
            alpha = 0
            epsilon = 0.1
            for line in f:
                x = [int(x) for x in line.split()]
                affinity.append(x)
            print(spectral_sklearn.solve(affinity, n, m, k, epsilon, 10000))
            print(greedy.solve(affinity, n,m,k,epsilon,500))
            print(greedy.solve(affinity, n,m,k,epsilon,1000))
            print(greedy_KL.solve(affinity, n, m, k, epsilon, 10000))
            print()


def set1000():
    for i in range(1, 21):
        with open(f"../data/1000ver_denser/test{i}.txt") as f:
            print(f"TEST {i}:")
            affinity = list()
            n = 50
            m = 125
            k = 2
            alpha = 0
            epsilon = 0.1
            for line in f:
                x = [int(x) for x in line.split()]
                affinity.append(x)
            print(greedy.solve(affinity, n,m,k,epsilon,500))
            print(greedy.solve(affinity, n,m,k,epsilon,1000))
            print(greedy_KL.solve(affinity, n, m, k, epsilon, 10000))
    pass


if __name__ == '__main__':
    output_path = "../data/bipartition_result.txt"
    with open(output_path, "w") as o:
        with contextlib.redirect_stdout(o):
            print("SET 1")
            set10()
            print("SET 2")
            set20()
            print("SET 3")
            set50sparse()
            print("SET 4")
            set50dense()
            # print("SET 5")
            # set100sparse()
            # print("SET 6")
            # set100dense()
            # print("SET 7")
            # set1000()