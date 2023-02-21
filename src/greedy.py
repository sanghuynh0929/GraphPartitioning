import random
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

def solve(affinity, n, m, k, epsilon, epochs):
    min_ans = float('inf')
    for epoch in range(epochs):
        P0, P1 = greedy_partition(affinity, n, 2)
        ans = 0
        for p in P0:
            for q in P1:
                ans += affinity[p][q]
        min_ans = min(ans, min_ans)
    return min_ans
