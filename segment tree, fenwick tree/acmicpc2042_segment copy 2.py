# Segment Tree
# 설명 지운 버전.
import sys
input=sys.stdin.readline

N, M, K = map(int, input().split())

A = [int(input()) for _ in range(N)]
tree = [0]*(4*N)

def init(left, right, node):
    if left == right:
        tree[node] = A[left]
        return tree[node]
    mid = (left+right)//2
    tree[node] = init(left, mid, node*2) + init(mid+1, right, node*2+1)
    return tree[node]

def interval_sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right: 
        return tree[node]
    mid = (start+end)//2
    return interval_sum(start, mid, node*2, left, right) + interval_sum(mid+1, end, node*2+1, left, right)

def update(start, end, node, index, diff):
    if end < index or start > index:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start+end)//2
    update(start, mid, node*2, index, diff)
    update(mid+1, end, node*2+1, index, diff)

init(0, N-1, 1)

answers = []
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, N, 1, b, c-A[b-1])
        A[b-1] = c
    else:
        answers.append(interval_sum(1, N, 1, b, c))

print(*answers, sep='\n')