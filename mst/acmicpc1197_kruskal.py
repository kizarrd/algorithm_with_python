# kruskal's
import sys
input=sys.stdin.readline

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])

parents = list(range(V+1))

def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    if fa < fb:
        parents[fb] = fa
    else:
        parents[fa] = fb

cnt = 0
weights = 0
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        weights += w
        cnt += 1
        if cnt == V-1:
            break

print(weights)