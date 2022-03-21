import sys
input=sys.stdin.readline

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

start, end = 1, houses[-1]
distance = 0
while start <= end:
    mid = (start+end)//2

    prev = houses[0]
    cnt = 1
    for i in range(1, N):
        if houses[i] - prev >= mid:
            cnt += 1
            prev = houses[i]
    
    if cnt >= C:
        distance = mid
        start = mid+1
    else:
        end = mid-1

print(distance)