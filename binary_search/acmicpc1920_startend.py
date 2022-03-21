import sys
input=sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums_to_search = list(map(int, input().split()))
A.sort()

def binary_search(n, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if n == A[mid]:
        return 1
    elif n < A[mid]:
        return binary_search(n, start, mid-1)
    elif n > A[mid]:
        return binary_search(n, mid+1, end)

for n in nums_to_search:
    print(binary_search(n, 0, N-1))