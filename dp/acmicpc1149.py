import sys
input=sys.stdin.readline

N = int(input())
cost = [0]+[list(map(int, input().split())) for _ in range(N)]
d = [0]*(N+1)
d[1] = cost[1][:] # d[i] = [mincost when house i is painted by Red, Green, Blue]

for i in range(2, N+1):
    d[i] = [min(cost[i][0]+d[i-1][1], cost[i][0]+d[i-1][2]), min(cost[i][1]+d[i-1][0], cost[i][1]+d[i-1][2]), min(cost[i][2]+d[i-1][0], cost[i][2]+d[i-1][1])]

print(min(d[N]))