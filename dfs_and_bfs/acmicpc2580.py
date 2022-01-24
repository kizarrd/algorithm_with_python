import sys
input=sys.stdin.readline
sdk = [list(map(int, input().split())) for _ in range(9)]

blanks = []
for r in range(9):
    for c in range(9):
        if sdk[r][c] == 0:
            blanks.append((r, c))

len_blanks = len(blanks)
def dfs(node_idx):
    if node_idx == len_blanks:
        for i in range(9):
            print(*sdk[i])
        exit()
    R, C = blanks[node_idx]
    candidates = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }

    r_low = 3*(R//3)
    c_low = 3*(C//3)
    for r in range(r_low, r_low+3):
        for c in range(c_low, c_low+3):
            candidates.discard(sdk[r][c])
    
    candidates -= set(sdk[R])
    candidates -= set([sdk[r][C] for r in range(9)])

    if not candidates:
        return
    for candi in candidates:
        sdk[R][C] = candi
        dfs(node_idx+1)
        sdk[R][C] = 0

dfs(0)