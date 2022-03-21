from collections import defaultdict
import sys
input=sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sums_A = defaultdict(int)
sums_B = defaultdict(int)

#inefficient
for len_sub in range(1, len(A)+1):
    for left in range(len(A)-len_sub+1):
        sums_A[sum(A[left:left+len_sub])] += 1

for len_sub in range(1, len(B)+1):
    for left in range(len(B)-len_sub+1):
        sums_B[sum(B[left:left+len_sub])] += 1

cnt = 0
for sB in sums_B:
    if T-sB in sums_A:
        cnt += sums_B[sB]*sums_A[T-sB]

print(cnt)