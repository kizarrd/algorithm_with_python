from heapq import heappush, heappop
import sys
input=sys.stdin.readline

N, M = map(int, input().split())
bridges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    heappush(bridges, (-C, A, B))
fact1, fact2 = map(int, input().split())

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    if fa > fb:
        parents[fa] = fb
    else:
        parents[fb] = fa

def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]

parents = list(range(N+1))
while bridges:
    C, A, B = heappop(bridges)
    C = -C
    union(A, B)
    if find(fact1) == find(fact2):
        print(C)
        break