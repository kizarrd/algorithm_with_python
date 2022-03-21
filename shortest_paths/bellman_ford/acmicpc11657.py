import math
import sys
input=sys.stdin.readline

N, M = map(int, input().split())

edges = []

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

# bellman-ford
dist = [math.inf]*(N+1) # distance from start node to each node
def bf(start):
    dist[start] = 0 
    for i in range(N):
        for a, b, c in edges:
            if dist[a] != math.inf and dist[a]+c < dist[b]:
                dist[b] = dist[a]+c
                if i == N-1:
                    return True
    return False

negative_cycle = bf(1)
if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == math.inf:
            print(-1)
        else:
            print(dist[i])