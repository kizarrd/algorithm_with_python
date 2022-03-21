import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

T = int(input())

def dfs(r, path):
    if visited[r]: # cycle formed
        a = path.index(r)
        for j in range(a): cant_make_team.add(path[j])
        for j in range(a, len(path)): made_team.add(path[j])
        return
    if r in made_team or r in cant_make_team:
        for p in path: cant_make_team.add(p)
        return
    visited[r] = True
    path.append(r)
    dfs(s[r], path)
    visited[r] = False

for _ in range(T):
    n = int(input())
    s = [0]+list(map(int, input().split()))
    visited = [False]*(n+1)
    made_team = set()
    cant_make_team = set()
    for i in range(1, n+1):
        if i not in made_team and i not in cant_make_team:
            path = []
            dfs(i, path)
    print(n-len(made_team))