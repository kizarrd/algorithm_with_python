import sys
input=sys.stdin.readline

T = int(input())

def dfs(n):
    stack = []
    stack.append(n)
    visited[n] = 1
    while stack:
        next = stack.pop()
        if not visited[p[next]]:
            visited[p[next]] = 1
            stack.append(p[next])

answers = []

for _ in range(T):
    N = int(input())
    p = [0]+list(map(int, input().split()))
    visited = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    answers.append(cnt)

print(*answers, sep='\n')