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
    global lower_bound, ans_partition

    def check_valid_partition():
        def check_alpha(cnt):
            mn = min(cnt)
            mx = max(cnt)
            if mx - mn <= alpha:
                return True
            return False

        count = [0 for _ in range(k)]
        for i in range(n):
            count[partition[i]] += 1
        if setting == 0:
            return check_alpha(count)
        else:
            return check_epsilon(count)

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


def solve(input_affinity, input_n, input_m, input_k, input_alpha):
    global affinity, n, m, k, alpha, partition, ans_partition

    affinity = input_affinity
    n = input_n
    m = input_m
    k = input_k
    alpha = input_alpha
    partition = [0 for i in range(n)]
    ans_partition = [-1 for i in range(n)]
    Try(0, 0)
    return ans_partition

