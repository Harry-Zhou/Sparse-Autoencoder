
import numpy as np
from scipy.io import savemat
from scipy.sparse import coo_matrix

f = open('out.advogato', 'r')
row = []
col = []
data = []
for line in f.readlines():
    line = line.strip()
    if line.find('%') == -1:
        ui, uj, trust = line.split(" ")
        row.append(int(ui)-1)
        col.append(int(uj)-1)
        data.append(float(trust))

adj_mat = coo_matrix((data, (row, col)))
savemat('data.mat', dict(data=data))
