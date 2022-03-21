from heapq import heappush, heappop
import sys
input=sys.stdin.readline

N = int(input())
stations = [list(map(int, input().split())) for _ in range(N)]
L, P = map(int, input().split())
stations.sort()

passed = []
visited = 0
fuel = P
distance_reachable = P
i = 0
while distance_reachable < L:
    while i < N and stations[i][0] <= distance_reachable:
        heappush(passed, -stations[i][1])
        i += 1
    if not passed: 
        break
    b = -heappop(passed)
    distance_reachable += b
    visited += 1

print(visited if distance_reachable >= L else -1)