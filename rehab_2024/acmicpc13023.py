from collections import defaultdict
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

adj_list = defaultdict(list)
for _ in range(M):
  v, w = map(int, input().split())
  adj_list[v].append(w)
  adj_list[w].append(v)

visited = [0]*N
def dfs(v, depth=0):
  global visited
  if depth == 4:
    print(1)
    sys.exit()
  for w in adj_list[v]:
    if visited[w] == 0:
      visited[w] = 1
      dfs(w, depth+1)
      visited[w] = 0

for v in range(N):
  if v in adj_list:
    visited = [0]*N
    visited[v] = 1
    dfs(v)

print(0)