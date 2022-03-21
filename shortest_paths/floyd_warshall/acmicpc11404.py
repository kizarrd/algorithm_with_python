import math
import sys
input=sys.stdin.readline

n = int(input())
m = int(input())
costs = [[math.inf]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < costs[a][b]:
        costs[a][b] = c
for i in range(1, n+1):
    costs[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and costs[i][k]+costs[k][j] < costs[i][j]:
                costs[i][j] = costs[i][k]+costs[k][j]
                
for i in range(1, n+1):
    for j in range(1, n+1):
        if costs[i][j] == math.inf:
            print(0, end='')
        else:
            print(costs[i][j], end='')
        if j < n:
            print(' ', end='')
    print()