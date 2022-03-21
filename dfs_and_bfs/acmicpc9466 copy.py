import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

T = int(input())

def dfs(r, path):
    global made_team
    if visited[r]: # 이미 방문한 경우엔 다음 두가지가 있다: 1.새로운 cycle, 즉 새로운 팀을 찾았거나 2.전에 팀을 찾지 못한 녀석이거나
        if r in path: # path안에 있다면 새로운 cycle을 찾은 경우이다. 
            made_team += (len(path) - path.index(r))
        return # 2번경우에도 경우에도 종료하여야 한다.

    visited[r] = True
    path.append(r)
    dfs(s[r], path)

for _ in range(T):
    n = int(input())
    s = [0]+list(map(int, input().split()))
    visited = [False]*(n+1)
    made_team = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, [])

    print(n-made_team)