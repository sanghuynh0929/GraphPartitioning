import random

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
            pair = []

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
    return P0, P1

def solve(affinity, n, m, k, epsilon, time):
    P0, P1 = greedy_partition(affinity, n, 2)
    P0_, P1_ = KL(affinity, P0, P1)
    ans = 0
    for p in P0_:
        for q in P1_:
            ans += affinity[p][q]
    return ans




def greedy_partition(graph, n, k):
    part = [-1] * n
    vert = list(range(n))
    random.shuffle(vert)

    for p in range(2):
        u = vert[-1]
        part[u] = p
        vert.pop()

    p = 0

    def total_gain(P,p,v,G):
        ans = 0
        for u in P:
            if P[u] != p and P[u] != -1:
                ans += G[v][u]
                # Gain
        return ans

    def greedy(V, P, p, G):
        m = float('inf')
        C = []
        gain = [0] * len(V)
        for i, v in enumerate(V):
            g = total_gain(P,p,v,G)
            m = min(m,g)
            gain[i] = g
        for i in range(len(V)):
            if gain[i] == m:
                C.append(V[i])
        return random.choice(C)

    while len(vert) > 0:
        b = greedy(vert, part, p, graph)
        part[b] = p
        vert.remove(b)
        p = (p + 1) % k
    P0, P1 = set(), set()
    for i in range(len(part)):
        if part[i] == 0:
            P0.add(i)
        else:
            P1.add(i)
    return P0, P1

