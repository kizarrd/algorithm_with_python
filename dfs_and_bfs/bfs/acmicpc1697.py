#숨바꼭질
from collections import deque

n, k = map(int, input().split())
visited = [False]*(100001)
def getTimeByBfs(n, k):
    if n==k:
        return 0
    deq = deque()
    deq.append([n, 0])
    while deq:
        current = deq.popleft()
        currentPosition = current[0]
        currentTime = current[1]
        if currentPosition == k:
            return currentTime
        if -1<currentPosition-1 and not visited[currentPosition-1]:
            deq.append([currentPosition-1, currentTime+1])
            visited[currentPosition-1]=True
        if 100001>currentPosition+1 and not visited[currentPosition+1]:
            deq.append([currentPosition+1, currentTime+1])
            visited[currentPosition+1]=True
        if 100001>currentPosition*2 and not visited[currentPosition*2]:
            deq.append([currentPosition*2, currentTime+1])
            visited[currentPosition*2]=True

print(getTimeByBfs(n, k))