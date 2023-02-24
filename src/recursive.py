from random import shuffle
from copy import deepcopy
def KL(adj, P0, P1):
    improvement = True
    iteration = 50000

    def Ex(u, P):
        # external cost
        cost = 0
        for v in P:
            cost += adj[u][v]
        return cost

    def In(u, P):
        # internal cost
        cost = 0
        for v in P:
            cost += adj[u][v]
        return cost

    def gP_u(u, P, P_):
        return Ex(u, P_) - In(u, P)
    n = len(adj)
    while improvement and iteration > 0:
        g = dict()
        for u in P0:
            g[u] = gP_u(u, P0, P1)
        for v in P1:
            g[v] = gP_u(v, P1, P0)

        L0 = set()
        L1 = set()

        gains = []

        for _ in range(n // 2):
            max_gain = -1 * float('inf')
            pair = None

            for u in P0:
                if u not in L0:
                    for v in P1:
                        if v not in L1:
                            gain = g[u] + g[v] - 2 * adj[u][v]
                            if gain > max_gain:
                                max_gain = gain
                                pair = (u,v)
            a = pair[0]
            b = pair[1]
            L0.add(a)
            L1.add(b)
            gains.append(((a,b), max_gain))

            for u in P0:
                if u not in L0:
                    g[u] += 2 * adj[u][a] - 2 * adj[u][b]

            for v in P1:
                if v not in L1:
                    g[v] += 2 * adj[v][b] - 2 * adj[v][a]

        gmax = -1 * float('inf')
        jmax = 0
        for j in range(1, len(gains) + 1):
            gsum = 0
            for i in range(j):
                gsum += gains[i][1]
            if gsum > gmax :
                gmax = gsum
                jmax = j


        if gmax > 0:
            for i in range(jmax):
                P0.remove(gains[i][0][0])
                P0.add(gains[i][0][1])
                P1.remove(gains[i][0][1])
                P1.add(gains[i][0][0])
        else:
            improvement = False
        iteration -= 1
    return

def rndpartition(n):
    part = [0 for i in range(n)]
    for i in range(n // 2):
        part[i] = 1
    shuffle(part)
    P0, P1 = set(), set()
    for i in range(n):
        if part[i] == 0:
            P0.add(i)
        else:
            P1.add(i)
    return P0, P1

def bipartitioner(graph, n):
    P0, P1 = rndpartition(n)
    KL(graph, P0, P1)
    return P0, P1

def generate_subgraph(matrix, indices):
    submatrix = [[matrix[i][j] for j in indices] for i in indices]
    return submatrix

def recurse(graph, n, k):
    part = [1 for _ in range(n)]
    it = 1
    while 1 << (it - 1) != k:
        # After this iteration, each number x in part would become x*2 or x*2+1
        for j in range(1 << (it - 1), 1 << it):
            fn = dict()
            ivfn = dict()
            counter = 0
            for p in range(n):
                if part[p] == j:
                    fn[p] = counter
                    ivfn[counter] = p
                    counter += 1
            subgraph = generate_subgraph(graph, fn)
            subsize = len(fn)
            P0, P1 = bipartitioner(subgraph, subsize)
            P0 = set(ivfn[i] for i in P0)
            P1 = set(ivfn[i] for i in P1)
            for p in range(n):
                if p in P0:
                    part[p] = part[p] * 2
                elif p in P1:
                    part[p] = part[p] * 2 + 1
        it += 1
    return [x - k for x in part]

def solve(graph, n, m, k, alpha, timelimit):
    # Check if k is power of 2
    if not (k and (not (k & (k - 1)))):
        raise Exception("k must be power of 2")
    part = recurse(deepcopy(graph), n, k)
    ans = 0
    for i in range(n):
        for j in range(i):
            if part[i] != part[j]:
                ans += graph[i][j]
    return ans


