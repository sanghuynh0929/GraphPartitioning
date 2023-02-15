from ortools.linear_solver import pywraplp
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


def solve(input_affinity, input_n, input_m, input_k, input_epsilon, inp_time_limit=None):
    global affinity, n, m, k, epsilon, V_max
    global xadj, adjncy, vwgt, adjcwgt
    global time_limit

    time_limit = inp_time_limit
    affinity = deepcopy(input_affinity)
    n = input_n
    m = input_m
    k = input_k
    epsilon = input_epsilon
    V_max = ceil((1 + epsilon) * n / k)
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
    IPModel()

    return ans_partition


def IPModel():
    global n, m, k, epsilon, V_max, partition, ans_partition, time_limit
    global xadj, adjncy, vwgt, adjcwgt

    solver = pywraplp.Solver.CreateSolver('SCIP')
    if time_limit:
        solver.set_time_limit(time_limit) # Time limit in ms
    infinity = solver.infinity()
    X = dict()
    E = dict()
    for v in range(n):
        for p in range(k):
            X[(v,p)] = solver.IntVar(0,1,'X[{},{}]'.format(v,p))
    for u in range(n):
        for j in range(xadj[u], xadj[u+1]):
            v = adjncy[j]
            if u < v:
                E[(u,v)] = solver.IntVar(0,1,'E[{},{}]'.format(u,v))


    for u,v in E:
        for p in range(k):
            solver.Add(E[u,v] >= X[u,p] - X[v,p])
            solver.Add(E[u,v] >= -X[u,p] + X[v,p])


    for p in range(k):
        constraint = solver.RowConstraint(0,V_max,'')
        for v in range(n):
            constraint.SetCoefficient(X[v,p], 1)

    for p in range(k):
        constraint = solver.RowConstraint(0,infinity,'')
        for v in range(n):
            constraint.SetCoefficient(X[v,p], 1)

    for v in range(n):
        constraint = solver.RowConstraint(1,1,'')
        for p in range(k):
            constraint.SetCoefficient(X[v,p], 1)

    objective = solver.Objective()
    for u,v in E:
        objective.SetCoefficient(E[(u,v)], int(affinity[u][v]))
    objective.SetMinimization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print('Objective Value =', solver.Objective().Value())
        for v in range(n):
            for p in range(k):
                if X[(v,p)].solution_value() == 1.:
                    print("Vertex {} belongs to Partition {}".format(v,p))
        print()
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
        print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
    else:
        print('The problem does not have an optimal solution.')
