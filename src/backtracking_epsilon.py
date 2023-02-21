from math import ceil
import copy
n = None
m = None
k = None
alpha = None
partition = None
ans_partition = None
affinity = None
lower_bound = float('inf')
V_max = None
epsilon = 0.05
def init():
    global affinity, n, m, k, alpha, partition, ans_partition, lower_bound, V_max, epsilon
    n = None
    m = None
    k = None
    alpha = None
    partition = None
    ans_partition = None
    affinity = None
    lower_bound = float('inf')
    V_max = None
    epsilon = 0.05

def Try(i, mx, ans=0):
    global lower_bound, ans_partition, V_max

    def check_valid_partition():
        count = [0 for _ in range(k)]
        for i in range(n):
            count[partition[i]] += 1
        return max(count) <= V_max

    if i == n:
        if check_valid_partition() is True and ans < lower_bound:
            ans_partition = partition[:]
            lower_bound = ans
    elif i == 0:
        partition[0] = 0
        Try(1,0,0)
    else:
        if mx == k-1:
            for j in range(k):
                new_ans = ans
                partition[i] = j
                # Update the weight
                for t in range(i):
                    if partition[t] != j:
                        new_ans += affinity[i][t]
                if new_ans <= lower_bound:
                    Try(i+1, k-1, new_ans)
                else:
                    continue

        elif (i-mx)+k == n + 1:
            new_ans = ans
            partition[i] = mx+1
            for t in range(i):
                if partition[t] != mx+1:
                    new_ans += affinity[i][t]
            if new_ans <= lower_bound:
                Try(i+1, mx+1, new_ans)
            else:
                return
        else:
            for j in range(mx+2):
                new_ans = ans
                partition[i] = j
                for t in range(i):
                    if partition[t] != j:
                        new_ans += affinity[i][t]
                if new_ans <= lower_bound:
                    Try(i+1, max(mx, j), new_ans)
                else:
                    continue


def solve(input_affinity, input_n, input_m, input_k, input_epsilon, time=0):
    global affinity, n, m, k, epsilon, V_max, partition, ans_partition
    init()
    affinity = copy.deepcopy(input_affinity)
    n = input_n
    m = input_m
    k = input_k
    epsilon = input_epsilon
    partition = [0 for i in range(n)]
    ans_partition = [-1 for i in range(n)]
    V_max = ceil((1 + epsilon) * n / k)
    Try(0, 0)
    return lower_bound, ans_partition

