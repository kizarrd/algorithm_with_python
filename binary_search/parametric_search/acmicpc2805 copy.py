import sys
input=sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
answer = 0
while start <= end:
    mid = (start+end)//2

    _sum = 0
    for height in trees:
        if height > mid:
            _sum += height-mid
    
    if _sum >= M:
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)