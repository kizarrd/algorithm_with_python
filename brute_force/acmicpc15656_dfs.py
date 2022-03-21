N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def dfs(d, combination):
    if d == M:
        print(combination.rstrip())
        return
    for i in range(N):
        dfs(d+1, combination+str(numbers[i])+' ')

dfs(0, '')