from bisect import bisect_left
import sys
input=sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
numbers = list(map(int, input().split()))

for target in numbers:
    i = bisect_left(A, target)
    if i < N and A[i] == target:
        print(1)
    else:
        print(0)