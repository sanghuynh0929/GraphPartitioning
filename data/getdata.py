def get_data(filename):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            data.append([int(x) for x in line.split()])
        n = data[0][0]
        m = data[0][1]
        k = data[0][2]
        alpha = data[0][3]        
        
        matrix = data[1:]
    return n, m, k, alpha, matrix
