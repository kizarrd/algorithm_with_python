import sys
input=sys.stdin.readline
N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

i, j = 0, 0
while i < N or j < M:
    if i < N and j == M:
        print(A[i], end=' ')
        i += 1
    elif j < M and i == N:
        print(B[j], end=' ')
        j += 1
    else:
        if A[i] < B[j]:
            print(A[i], end=' ')
            i += 1
        else:
            print(B[j], end=' ')
            j += 1
