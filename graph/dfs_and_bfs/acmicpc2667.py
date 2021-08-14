from collections import deque
import sys
input = sys.stdin.readline

mapSize = int(input())
matrix = [list(map(int, input().rstrip())) for _ in range(mapSize)]
visited = [ [False]*mapSize for _ in range(mapSize) ]
def bfs(x, y):
    deq = deque()
    deq.append((x,y))    
    visited[x][y] = True
    apartCount = 1
    while deq:
        coordinate = deq.popleft()
        a = coordinate[0]
        b = coordinate[1]
        if b-1 > -1 and matrix[b-1][a]==1 and not visited[a][b-1]:
            visited[a][b-1] = True
            deq.append((a, b-1))            
            apartCount+=1
        if a+1 < mapSize and matrix[b][a+1]==1 and not visited[a+1][b]:
            visited[a+1][b] = True
            deq.append((a+1, b))            
            apartCount+=1
        if b+1 < mapSize and matrix[b+1][a]==1 and not visited[a][b+1]:
            visited[a][b+1] = True
            deq.append((a, b+1))            
            apartCount+=1
        if a-1 > -1 and matrix[b][a-1]==1 and not visited[a-1][b]:
            visited[a-1][b] = True
            deq.append((a-1, b))            
            apartCount+=1
    return apartCount

groupCount=0
apartlist = []

for y in range(mapSize):
    for x in range(mapSize):
        if matrix[y][x]==1 and not visited[x][y]:
            apartlist.append(bfs(x, y))
            groupCount+=1

print(groupCount)
apartlist.sort()
for apartCount in apartlist:
    print(apartCount)