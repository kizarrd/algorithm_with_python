N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
uniques = set()
answers = []
def dfs(d, seq):
    if d == M:
        if (stripped:=seq.rstrip()) not in uniques:
            uniques.add(stripped)
            answers.append(stripped)
        return

    for i in range(len(numbers)):
        e = numbers[i]
        del numbers[i]
        dfs(d+1, seq+str(e)+' ')
        numbers.insert(i, e)

dfs(0, '')

print(*answers, sep='\n')