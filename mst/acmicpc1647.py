import sys
input=sys.stdin.readline

N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]
roads.sort(key=lambda x: x[2])

parents = list(range(N+1))
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

max_weight = 0
total_weight = 0
cnt = 0
for u, v, w in roads:
    if find(u) != find(v):
        union(u, v)
        max_weight = max(max_weight, w)
        total_weight += w
        cnt += 1
        if cnt == N-1:
            break

print(total_weight - max_weight)