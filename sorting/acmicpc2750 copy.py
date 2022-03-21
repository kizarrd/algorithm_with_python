from heapq import heappush, heappop
N = int(input())
A = []
for _ in range(N):
    heappush(A, int(input()))
while A:
    print(heappop(A))