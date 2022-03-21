N, M = map(int, input().split())
N_numbers = list(map(int, input().split()))
N_numbers.sort()

permutation = []
visited = [0]*N
def dfs(depth):
    if depth == M:
        print(*permutation)
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            permutation.append(N_numbers[i])
            dfs(depth+1)
            visited[i] = 0
            permutation.pop()

dfs(0)