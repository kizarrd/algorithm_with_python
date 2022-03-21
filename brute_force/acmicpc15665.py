N, M = map(int, input().split())
numbers = list(set(list(map(int, input().split()))))
numbers.sort()
N = len(numbers)

def dfs(d, seq):
    if d == M:
        print(seq.rstrip())
        return
    
    for i in range(N):
        dfs(d+1, seq+str(numbers[i])+' ')

dfs(0, '')