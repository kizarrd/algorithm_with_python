from collections import defaultdict
import sys
input=sys.stdin.readline
size = int(input())
m, n = map(int, input().split())
A, B = [], []
for _ in range(m):
    A.append(int(input()))
for _ in range(n):
    B.append(int(input()))

sum_A = defaultdict(int)
sum_A[0] = 1
sum_A[sum(A)] = 1

for i in range(m):
    _sum = 0
    for j in range(i, i+m-1):
        k = j
        if j >= m:
            k = j%m
        _sum+=A[k]
        if _sum > size:
            break
        sum_A[_sum]+=1

answer = 0

for i in range(n):
    _sum = 0
    for j in range(i, i+n-1):
        k = j
        if j >= n:
            k = j%n
        _sum+=B[k]
        if _sum > size:
            break
        answer += sum_A[size-_sum]

if (a:=sum_A[size]) > 0:
    answer += a
if sum_A[size-(b:=sum(B))] > 0:
    answer += sum_A[size-b]

print(answer)