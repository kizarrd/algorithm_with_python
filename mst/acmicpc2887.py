from heapq import heappush, heappop
import sys
input=sys.stdin.readline

N = int(input())
planets = set()
for i in range(1, N+1):
    x, y, z = map(int, input().split())
    planets.add((i, x, y, z))

hq = []
i, x, y, z = 0, 0, 0, 0
for e in planets:
    i, x, y, z = e
    break
heappush(hq, (0, i, x, y, z)) # cost, id, x, y, z
visited = [0]*(N+1)
total_cost = 0
cnt = 0
while hq:
    c, i, x, y, z = heappop(hq)
    if not visited[i]:
        visited[i] = 1
        planets.remove((i, x, y, z))
        total_cost += c
        cnt += 1
        if cnt == N:
            break
        for i2, x2, y2, z2 in planets:
            cost = min(abs(x2-x), abs(y2-y), abs(z2-z))
            heappush(hq, (cost, i2, x2, y2, z2))

print(total_cost)