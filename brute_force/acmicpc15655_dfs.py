N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def dfs(d, prev, combination):
    if d == M:
        print(combination.rstrip())
    for i in range(prev+1, N):
        dfs(d+1, i, combination+str(numbers[i])+' ')

dfs(0, -1, '')