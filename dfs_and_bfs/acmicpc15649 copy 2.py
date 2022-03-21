N, M = map(int, input().split())

visited = [0]*(N+1)
permutation = []

def dfs():
    if len(permutation) == M:
        print(*permutation)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            permutation.append(i)
            dfs()
            permutation.pop()
            visited[i] = 0

dfs()