from heapq import heappush, heappop
import sys
input=sys.stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
C = [int(input()) for _ in range(K)]
jewels.sort()
C.sort()

take_ables = []
price = 0
i = 0
for c in C:
    while i<N and jewels[i][0] <= c:
        heappush(take_ables, -jewels[i][1])
        i += 1
    if take_ables:
        price += -heappop(take_ables)

print(price)