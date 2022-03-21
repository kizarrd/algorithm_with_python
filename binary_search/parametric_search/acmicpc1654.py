import sys
input=sys.stdin.readline

K, N = map(int, input().split())
lan_cables = []
for _ in range(K):
    lan_cables.append(int(input()))

start, end = 1, max(lan_cables)
answer = 0

while start <= end:
    mid = (start+end)//2

    cnt = 0
    for cable in lan_cables:
        if cable >= mid:
            cnt += cable//mid
    
    if cnt >= N:
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)