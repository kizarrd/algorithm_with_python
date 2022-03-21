import sys
input=sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
numbers = list(map(int, input().split()))

def binary_search(n, i, j):
    if j-i == 1:
        if n == A[i]:
            return 1
        else:
            return 0

    mid = (i+j)//2
    if n >= A[mid]:
        return binary_search(n, mid, j)
    else:
        return binary_search(n, i, mid)

for n in numbers:
    print(binary_search(n, 0, N))