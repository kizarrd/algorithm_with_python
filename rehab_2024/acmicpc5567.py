from collections import defaultdict
import sys
input=sys.stdin.readline

n = int(input())
m = int(input())

adj_list = defaultdict(list)
for _ in range(m):
  a, b = map(int, input().split())
  adj_list[a].append(b)
  adj_list[b].append(a)

invite = [1]
visited = [0]*(n+1)
visited[1]=1
def dfs(v, depth=1):
  if depth > 2:
    return
  for w in adj_list[v]:
    if visited[w] == 0:
      visited[w] = 1
      if w not in invite:
        invite.append(w)
      dfs(w, depth+1)
      visited[w] = 0

dfs(1)
print(len(invite)-1)