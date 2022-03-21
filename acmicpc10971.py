import math
N = int(input())
W = [0]+[[0]+list(map(int, input().split())) for _ in range(N)]

def dfs(n, cost):
    global start, _min
    for j in range(1, N+1):
        if W[n][j] != 0:
            if not visited[j] and cost+W[n][j] < _min:
                visited[j] = 1
                dfs(j, cost+W[n][j])
                visited[j] = 0
            elif j == start and all(visited):
                _min = min(_min, cost+W[n][j])
                return

_min = math.inf
start = 1
visited = [0]*(N+1)
visited[0], visited[1] = 1, 1 # check visited[0] as well, in order to use function all
dfs(1, 0)
print(_min)