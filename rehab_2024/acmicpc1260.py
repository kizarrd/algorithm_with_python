from collections import defaultdict
import sys
input=sys.stdin.readline

N, M, V = map(int, input().split())

adj_list = defaultdict(list)
for _ in range(M):
  v, w = map(int, input().split())
  adj_list[v].append(w)
  adj_list[w].append(v)

for key in adj_list.keys():
  adj_list[key].sort()

dfs_discovered = []
visited = [0]*(N+1)
def dfs(v):
  global dfs_discovered, visited
  dfs_discovered.append(v)
  visited[v] = 1
  for w in adj_list[v]:
    if visited[w] == 0:
      dfs(w)

bfs_discovered = []
queue = []
def bfs(start_v):
  global queue, bfs_discovered, visited
  bfs_discovered.append(start_v)
  visited[start_v] = 1
  queue.append(start_v)
  while queue:
    v = queue.pop(0)
    for w in adj_list[v]:
      if visited[w] == 0:
        bfs_discovered.append(w)
        visited[w] = 1
        queue.append(w)
      
dfs(V)
visited = [0]*(N+1)
bfs(V)
print(*dfs_discovered)
print(*bfs_discovered)