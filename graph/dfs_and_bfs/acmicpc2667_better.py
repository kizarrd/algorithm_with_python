from collections import deque
import sys
input = sys.stdin.readline

mapSize = int(input())
matrix = [list(map(int, input().rstrip())) for _ in range(mapSize)]
visited = [[False]*mapSize for _ in range(mapSize)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
groupCount=0
apartCountlist = []

def bfs(x, y):
    deq = deque()
    deq.append((x, y))
    visited[x][y] = True
    apartCount = 1
    while deq:
        coordinate = deq.popleft()
        for i in range(4):
            nx = coordinate[0]+dx[i]
            ny = coordinate[1]+dy[i]
            if -1 <nx<mapSize and -1<ny<mapSize:
                if matrix[nx][ny]==1 and not visited[nx][ny]:
                    deq.append((nx, ny))
                    visited[nx][ny]=True
                    apartCount+=1
    return apartCount

for x in range(mapSize):
    for y in range(mapSize):
        if matrix[x][y]==1 and not visited[x][y]:
            apartCountlist.append(bfs(x, y))
            groupCount+=1

print(groupCount)
apartCountlist.sort()
for apartCount in apartCountlist:
    print(apartCount)