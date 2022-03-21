N, M = map(int, input().split())

permutation = []
def dfs(l):
    if l == M:
        print(' '.join(map(str, permutation)))
        return

    for i in range(1, N+1):
        permutation.append(i)
        dfs(l+1)
        permutation.pop()

dfs(0)