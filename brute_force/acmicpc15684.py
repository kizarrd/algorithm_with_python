from bisect import insort
import sys
input=sys.stdin.readline

N, M, H = map(int, input().split())
ladders = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    ladders[b].append((a, b+1))
    ladders[b+1].append((a, b))

for vertical in ladders:
    vertical.sort()

def placeable(a, b, ladders):
    if b > 0 and (a, b-1) in ladders[b]:
        return False
    if b < N-1 and (a, b+1) in ladders[b]:
        return False
    return True

def get_destination(i, height, ladders):
    for a, b in ladders[i]:
        if a > height:
            return get_destination(b, a, ladders)
    return i

def satisfied(ladders):
    for i in range(1, N+1):
        if get_destination(i, 0, ladders) != i:
            return False
    return True

_min = 4
def dfs(d, prev, ladders):
    global _min
    if d >= _min:
        return
    if satisfied(ladders):
        _min = min(_min, d)
        return
    elif d == 3:
        return

    ladders_copy = []
    for vertical in ladders:
        ladders_copy.append(vertical[:])

    for i in range(prev+1, (N-1)*H):
        a, b = i//(N-1)+1, i%(N-1)+1
        if (a, b+1) not in ladders_copy[b] and placeable(a, b, ladders_copy):
            insort(ladders_copy[b], (a, b+1))
            insort(ladders_copy[b+1], (a, b))
            dfs(d+1, i, ladders_copy)
            ladders_copy = []
            for vertical in ladders:
                ladders_copy.append(vertical[:])

dfs(0, -1, ladders)

print(_min if _min < 4 else -1)