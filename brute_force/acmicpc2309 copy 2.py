# dfs
dwarfs = [int(input()) for _ in range(9)]

answer = None

def dfs(c):
    global answer
    if answer:
        return
    if len(c) == 7:
        if sum(c) == 100:
            answer = c
        return
    for e in c[:]:
        c.remove(e)
        c_copy = c[:]
        dfs(c_copy)
        c.append(e)

dfs(dwarfs)
print(*sorted(answer), sep='\n')