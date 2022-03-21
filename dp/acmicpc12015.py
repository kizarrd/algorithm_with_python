from bisect import bisect_left
import sys
input=sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

seq = [A[0]]

for i in range(1, N):
    if A[i] > seq[-1]:
        seq.append(A[i])
    else:
        j = bisect_left(seq, A[i])
        seq[j] = A[i]

print(len(seq))