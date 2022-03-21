N, M = map(int, input().split())

permutation = []
def dfs(prev, l):
    if l == M:
        print(' '.join(map(str, permutation)))
        return

    for i in range(prev, N+1):
        permutation.append(i)
        dfs(i, l+1)
        permutation.pop()

dfs(1, 0)