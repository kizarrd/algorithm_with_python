import math
import sys
input=sys.stdin.readline

N, M = map(int, input().split())

A = [int(input()) for _ in range(N)]
min_tree = [0]*(4*N)
max_tree = [0]*(4*N)

def init_min(left, right, node):
    if left == right:
        min_tree[node] = A[left]
        return min_tree[node]
    mid = (left+right)//2
    min_tree[node] = min(init_min(left, mid, node*2), init_min(mid+1, right, node*2+1))
    return min_tree[node]

def init_max(left, right, node):
    if left == right:
        max_tree[node] = A[left]
        return max_tree[node]
    mid = (left+right)//2
    max_tree[node] = max(init_max(left, mid, node*2), init_max(mid+1, right, node*2+1))
    return max_tree[node]

def interval_min(start, end, node, left, right):
    if start > right or end < left:
        return math.inf
    if left <= start and end <= right:
        return min_tree[node]
    mid = (start+end)//2
    return min(interval_min(start, mid, node*2, left, right), interval_min(mid+1, end, node*2+1, left, right))

def interval_max(start, end, node, left, right):
    if start > right or end < left:
        return -math.inf
    if left <= start and end <= right:
        return max_tree[node]
    mid = (start+end)//2
    return max(interval_max(start, mid, node*2, left, right), interval_max(mid+1, end, node*2+1, left, right))

init_min(0, N-1, 1)
init_max(0, N-1, 1)

answers = []
for _ in range(M):
    a, b = map(int, input().split())
    answers.append((interval_min(1, N, 1, a, b), interval_max(1, N, 1, a, b)))

for _min, _max in answers:
    print(_min, _max)