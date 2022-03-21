from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

nodes = [[0, 0, 0] for _ in range(n+1)] # (visited, max_depth, max_diameter)
_max = 0
def dfs(node):
    global _max
    nodes[node][0] = 1
    children = []
    for adj_v, adj_d in graph[node]:
        if not nodes[adj_v][0]:
            children.append(dfs(adj_v)+adj_d)
    if (_len:= len(children)) > 0:
        nodes[node][1] = max(children)
        if _len > 1:
            children.sort()
            nodes[node][2] = children[-1]+children[-2]
        elif _len == 1:
            nodes[node][2] = nodes[node][1]
        _max = max(_max, nodes[node][2])
        return nodes[node][1]
    else:
        return 0

dfs(1)
print(_max)