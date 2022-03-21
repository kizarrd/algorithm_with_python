# Kruskal
import sys
input=sys.stdin.readline

N = int(input())
planets = [[i]+list(map(int, input().split())) for i in range(0, N)] # i is planet id

# make edges for adjacent planets (adjacent by each of x, y, and z directions)
edges = [] # (u, v, w)
for dir in range(1, 4):
    planets.sort(key=lambda x: x[dir])
    for i in range(N-1):
        edges.append((planets[i][0], planets[i+1][0], abs(planets[i][dir]-planets[i+1][dir])))

edges.sort(key=lambda x: x[2])

parents = list(range(N))

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

total_cost = 0
cnt = 0
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        total_cost += w
        cnt += 1
        if cnt == N-1:
            break

print(total_cost)