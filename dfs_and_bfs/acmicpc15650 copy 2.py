N, M = map(int, input().split())
combination = []
def dfs(start, end):
    if len(combination) == M:
        print(*combination)
        return
    
    for i in range(start, end):
        combination.append(i)
        dfs(i+1, end+1)
        combination.pop()

dfs(1, N-M+2)