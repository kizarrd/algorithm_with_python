N, M = map(int, input().split())
numbers = list(set(list(map(int, input().split()))))
N = len(numbers)
numbers.sort()

def dfs(d, prev, seq):
    if d == M:
        print(seq.rstrip())
        return

    for i in range(prev, N):
        dfs(d+1, i, seq+str(numbers[i])+' ')

dfs(0, 0, '')