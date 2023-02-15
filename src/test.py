import CP_alpha_foreach
if __name__ == '__main__':
    with open('../data/50ver/test1.txt') as f:
        affinity = []
        for line in f:
            x = [int(x) for x in line.split()]
            affinity.append(x)
            n = 50
            m = 125
            k = 4
            epsilon = 0.05
        CP_alpha.solve(affinity, n, m, k, 4, 5000)