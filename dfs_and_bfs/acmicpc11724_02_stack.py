from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(N+1)
def dfs(n):
    visited[n] = 1
    stack = []
    stack.append(n)
    while stack:
        next_n = stack.pop()
        for adj_n in graph[next_n]:
            if not visited[adj_n]:
                visited[adj_n] = 1
                stack.append(adj_n)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)