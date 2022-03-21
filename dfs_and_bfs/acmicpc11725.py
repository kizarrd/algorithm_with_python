import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
N = int(input())
adj_list = [[] for _ in range(N+1)]
parents = [0]*(N+1)
parents[1] = 1

for _ in range(N-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def dfs(n):
    for adj_v in adj_list[n]:
        if not parents[adj_v]:
            parents[adj_v] = n 
            dfs(adj_v)

dfs(1)
for i in range(2, N+1):
    print(parents[i])