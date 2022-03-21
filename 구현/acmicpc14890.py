import sys
input=sys.stdin.readline
N, L = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]

placed = [[0]*N for _ in range(N)]
def placeable_row(r, start, end):
    if start < 0 or end >= N:
        return False
    height = _map[r][start]
    for i in range(start, end+1):
        if placed[r][i] or _map[r][i] != height:
            return False
        else:
            placed[r][i] = 1

    return True

cnt = 0
for r in range(N):
    for c in range(N):
        p = True
        if c+1 < N:
            if _map[r][c] == _map[r][c+1]:
                continue
            elif _map[r][c] - _map[r][c+1] == 1:
                p = placeable_row(r, c+1, c+L)
            elif _map[r][c] - _map[r][c+1] == -1:
                p = placeable_row(r, c-L+1, c)
            else:
                p = False
            if not p:
                break
    if p:
        cnt += 1


placed = [[0]*N for _ in range(N)]
def placeable_col(c, start, end):
    if start < 0 or end >= N:
        return False
    height = _map[start][c]
    for i in range(start, end+1):
        if placed[i][c] or _map[i][c] != height:
            return False
        else:
            placed[i][c] = 1

    return True

for c in range(N):
    for r in range(N):
        p = True
        if r+1 < N:
            if _map[r][c] == _map[r+1][c]:
                continue
            elif _map[r][c] - _map[r+1][c] == 1:
                p = placeable_col(c, r+1, r+L)
            elif _map[r][c] - _map[r+1][c] == -1:
                p = placeable_col(c, r-L+1, r)
            else:
                p = False
            if not p:
                break
    if p:
        cnt += 1

print(cnt)