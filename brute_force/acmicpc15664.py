N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

uniques = set()

def dfs(d, prev, seq):
    if d == M:
        stripped = seq.rstrip()
        if stripped not in uniques:
            uniques.add(stripped)
            print(stripped)
        return
    
    for i in range(prev+1, N):
        dfs(d+1, i, seq+str(numbers[i])+' ')

dfs(0, -1, '')