from ortools.sat.python import cp_model
from math import ceil
from copy import deepcopy

n = None
m = None
k = None
alpha = None
partition = None
ans_partition = None
affinity = None
V_max = None
epsilon = 0.05

xadj, adjncy, vwgt, adjcwgt = None, None, None, None
time_limit = None


def solve(input_affinity, input_n, input_m, input_k, input_alpha, inp_time_limit=None):
    global affinity, n, m, k, alpha, V_max
    global xadj, adjncy, vwgt, adjcwgt
    global time_limit

    time_limit = inp_time_limit
    affinity = deepcopy(input_affinity)
    n = input_n
    m = input_m
    k = input_k
    alpha = input_alpha
    xadj = [0]
    adjncy = []
    vwgt = [1]*n
    adjcwgt = []
    a = 0
    for i in range(n):
        for j in range(n):
            if affinity[i][j] != 0:
                adjncy.append(j)
                adjcwgt.append(affinity[i][j])
                a += 1
        xadj.append(a)
    CPModel()

    return ans_partition


def CPModel():
    global n, m, k, alpha, partition, ans_partition, time_limit
    global xadj, adjncy, vwgt, adjcwgt
    model = cp_model.CpModel()
    X = dict()
    E = dict()

    for v in range(n):
        for p in range(k):
            X[(v,p)] = model.NewIntVar(0,1,'X[{},{}]'.format(v,p))

    for u in range(n):
        for v in range(n):
            if affinity[u][v] !=0 and u < v:
                E[(u,v)] = model.NewIntVar(0, 1,'E[{},{}]'.format(u,v))

    for u,v in E:
        for p in range(k):
            model.Add(E[u,v] >= X[u,p] - X[v,p])
            model.Add(E[u,v] >= -X[u,p] + X[v,p])

    for v in range (n):
        model.Add(sum(X[(v,p)] for p in range(k)) == 1)

    mx = model.NewIntVar(0, n, 'mx')
    mn = model.NewIntVar(0, n, 'mn')
    for p in range(k):
        model.Add(sum(X[v,p] for v in range(n)) <= mx)
        model.Add(sum(X[v,p] for v in range(n)) >= mn)
    model.Add(mx - mn <= alpha)
    # for p in range(k):
    #     for q in range(k):
    #         model.Add(sum(X[(u,p)] for u in range(n)) - sum(X[(u,q)] for u in range(n)) <= alpha)

    model.Minimize(sum(E[u,v]*affinity[u][v] for u, v in E))
    solver = cp_model.CpSolver()
    if time_limit:
        solver.parameters.max_time_in_seconds = time_limit / 1000
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print('Objective Value =', solver.ObjectiveValue())
        for v in range(n):
            for p in range(k):
                if solver.Value(X[(v,p)]) == 1:
                    print("Vertex {} belongs to Partition {}".format(v,p))
    else:
        print('no feasible')
