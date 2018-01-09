# Dynamic Planning problem

 # 捡苹果。M*N的棋盘上，格子(i,j)上有a[i][j]个苹果，从(0,0)出发，每次只能向下或向右走一个，并拿走所在格子上的苹果，到终点(M-1,N-1)最多可以拿到多少苹果
M = 10
N = 10
a = [[]]

import numpy as np
values = np.zeros((M, N))
values[0, 0] = a[0][0]
for i in range(1, M):
    values[i, 0] = values[i-1, 0] + a[i][0]
for j in range(1, N):
    values[0, j] = values[0, j-1] + a[0][j]
for m in range(1, M):
    for n in range(1, N):
        val1 = values[m-1, n] + a[m][n]
        val2 = values[m, n-1] + a[m][n]
        values[m, n] = max(val1, val2)
print values[M-1, N-1]