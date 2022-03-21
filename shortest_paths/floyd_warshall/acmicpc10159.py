import math
import sys
INF = math.inf
input = sys.stdin.readline

N, M = int(input()), int(input())
A = [[0]*(N+1) for _ in range(N+1)] # A[i][j]의 값이 1이면 i가 j보다 무겁다는 것을 뜻하고, 0이면 알 수 없다는 것을 뜻한다.

for _ in range(M):
    a, b = map(int, input().split())
    A[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if A[i][k] and A[k][j]:
                A[i][j] = 1

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if not A[i][j] and not A[j][i]:
            cnt += 1
    print(cnt-1)