#섬의 개수
import sys
sys.setrecursionlimit(10**6)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        sys.exit(0)

    givenMap = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    countIslands=0

    def dfs(i, j):
        visited[i][j] = True
        for direction in range(8):
            nx=j+dx[direction]
            ny=i+dy[direction]
            if -1<nx<w and -1<ny<h:
                if not visited[ny][nx] and givenMap[ny][nx]==1:
                    dfs(ny,nx)

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and givenMap[i][j]==1:
                dfs(i, j)
                countIslands+=1
    
    print(countIslands)