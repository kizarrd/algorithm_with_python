#연결 요소
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    for adjNode in adjList[x]:
        if visited[adjNode] == False:
            dfs(adjNode)

n, m = map(int, input().split())
adjList = [[] for _ in range(n+1)]
visited = [False]*(n+1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)