from collections import defaultdict
import sys
input=sys.stdin.readline

V = int(input())
E = int(input())

adj_list = defaultdict(list)
for _ in range(E):
  u, v = map(int, input().split())
  adj_list[u].append(v)
  adj_list[v].append(u)

contaminated=[]
cnt = 0
def dfs(v):
  contaminated.append(v)
  for w in adj_list[v]:
    if w not in contaminated:
      dfs(w)

dfs(1)
print(len(contaminated)-1)