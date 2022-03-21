import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

N, M = map(int, input().split())
bridges = [list(map(int, input().split())) for _ in range(M)]
A, B = map(int, input().split())
bridges.sort(key=lambda x: x[2])

def get_idx(limit):
    lo, hi = 0, M
    while lo < hi:
        mid = (lo+hi)//2
        if bridges[mid][2] >= limit:
            hi = mid
        else:
            lo = mid+1
    return hi

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    if fa > fb:
        parents[fa] = fb
    else:
        parents[fb] = fa

def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]

lo, hi = 0, bridges[-1][2]
answer = 0
while lo <= hi:
    mid = (lo+hi)//2
    # get lower bound of islands pairs with limit >= mid
    lower_bound = get_idx(mid)
    # do union for island pairs connected by bridge with limit >= mid
    parents = list(range(N+1))
    for i in range(lower_bound, M):
        a, b, _ = bridges[i]
        union(a, b)
    # check if the two islands are connected and continue searching
    if find(A) == find(B):
        answer = mid
        lo = mid+1
    else:
        hi = mid-1

print(answer)