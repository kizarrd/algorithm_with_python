N, M = map(int, input().split())
combination = []
def dfs(start, l):
    if l == M:
        print(*combination)
        return
    
    for i in range(start, N-M+l+2):
        combination.append(i)
        dfs(i+1, l+1)
        combination.pop()

dfs(1, 0)