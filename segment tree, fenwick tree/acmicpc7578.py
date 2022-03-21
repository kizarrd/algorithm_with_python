import sys
input=sys.stdin.readline

N = int(input())
A = [0]+list(map(int, input().split()))
B = [0]+list(map(int, input().split()))
B_index = {}
for i in range(1, N+1):
    _id = B[i]
    B_index[_id] = i

tree = [0]*(N+1)

def update(i, n):
    diff = n
    while i <= N:
        tree[i] += diff
        i += (i & -i)

def prefix_sum(i):
    _sum = 0
    while i > 0:
        _sum += tree[i]
        i -= (i & -i)
    return _sum

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

cnt = 0
for i in range(1, N+1):
    bi = B_index[A[i]]
    update(bi, 1)
    cnt += interval_sum(bi+1, N)

print(cnt)