from collections import defaultdict
import sys
input=sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

adj_list = defaultdict(list)
for _ in range(m):
  x, y = map(int, input().split())
  adj_list[x].append(y)
  adj_list[y].append(x)

discovered = []
def dfs(v, depth):
  discovered.append(v)
  if v == b:
    print(depth)
    sys.exit()
  for w in adj_list[v]:
    if w not in discovered:
      dfs(w, depth+1)

dfs(a, 0)
print(-1)