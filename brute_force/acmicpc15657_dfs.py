N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def dfs(d, prev, combination):
    if d == M:
        print(combination.rstrip())
        return
    for i in range(prev, N):
        dfs(d+1, i, combination+str(numbers[i])+' ')

dfs(0, 0, '')