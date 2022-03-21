import sys
input=sys.stdin.readline
R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
path = ''
if R%2 == 1:
    path += ('R'*(C-1)+'D'+'L'*(C-1)+'D')*(R//2)+'R'*(C-1)
elif C%2 == 1:
    path += ('D'*(R-1)+'R'+'U'*(R-1)+'R')*(C//2)+'D'*(R-1)
else:
    # get the coordinates with the least happiness
    rl, cl = 0, 0
    val_least = 1001
    for i in range(R):
        for j in range(C):
            if (i+j)%2 == 1 and graph[i][j] < val_least:
                val_least = graph[i][j]
                rl, cl = i, j
    # get the path
    path += ('R'*(C-1)+'D'+'L'*(C-1)+'D')*(rl//2)
    path += 'DRUR'*(cl//2)
    if rl%2 == 0:
        path += 'DR'
    else: # rl%2 == 1
        path += 'RD'
    path += 'RURD'*(C//2-(cl//2 + 1))
    path += ('D'+'L'*(C-1)+'D'+'R'*(C-1))*(R//2-(rl//2+1))

print(path)