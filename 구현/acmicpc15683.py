from copy import deepcopy
N, M = map(int, input().split())
office = []
cctvs = []
for r in range(N):
    row = list(map(int, input().split()))
    office.append(row)
    for c in range(M):
        if 0 < row[c] < 6:
            cctvs.append((row[c], r, c))

def apply_cctv(office, r, c, top, right, bottom, left):
    if top:
        for i in range(r-1, -1, -1):
            if office[i][c] == 6:
                break
            elif office[i][c] == 0:
                office[i][c] = 7
    if right:
        for i in range(c+1, M):
            if office[r][i] == 6:
                break
            elif office[r][i] == 0:
                office[r][i] = 7
    if bottom:
        for i in range(r+1, N):
            if office[i][c] == 6:
                break
            elif office[i][c] == 0:
                office[i][c] = 7
    if left:
        for i in range(c-1, -1, -1):
            if office[r][i] == 6:
                break
            elif office[r][i] == 0:
                office[r][i] = 7

_min = N*M
def dfs(d, office):
    global _min
    if d == len(cctvs):
        cnt = 0
        for row in office:
            cnt += row.count(0)
        # if cnt < _min:
        #     print()
        #     for row in office:
        #         print(*row)
        _min = min(_min, cnt)
        return
    
    n, r, c = cctvs[d]

    office_copy = deepcopy(office)

    if n == 1:
        apply_cctv(office_copy, r, c, 1, 0, 0, 0)
        dfs(d+1, office_copy)
        office_copy = deepcopy(office)
        apply_cctv(office_copy, r, c, 0, 1, 0, 0)
        dfs(d+1, office_copy)
        office_copy = deepcopy(office)
        apply_cctv(office_copy, r, c, 0, 0, 1, 0)
        dfs(d+1, office_copy)
        office_copy = deepcopy(office)
        apply_cctv(office_copy, r, c, 0, 0, 0, 1)
        dfs(d+1, office_copy)
    elif n == 2:
        apply_cctv(office_copy, r, c, 1, 0, 1, 0)
        dfs(d+1, office_copy)
        office_copy = deepcopy(office)
        apply_cctv(office_copy, r, c, 0, 1, 0, 1)
        dfs(d+1, office_copy)
    elif n == 3:
        apply_cctv(office_copy, r, c, 1, 1, 0, 0)
        dfs(d+1, office_copy)
        office_copy = deepcopy(office)
        apply_cctv(office_copy, r, c, 0, 1, 1, 0)
        dfs(d+1, office_copy)
        office_copy = deepcopy(office)
        apply_cctv(office_copy, r, c, 0, 0, 1, 1)
        dfs(d+1, office_copy)
        office_copy = deepcopy(office)
        apply_cctv(office_copy, r, c, 1, 0, 0, 1)
        dfs(d+1, office_copy)
    elif n == 4:
        apply_cctv(office_copy, r, c, 1, 1, 0, 1)
        dfs(d+1, office_copy)
        office_copy = deepcopy(office)
        apply_cctv(office_copy, r, c, 1, 1, 1, 0)
        dfs(d+1, office_copy)
        office_copy = deepcopy(office)
        apply_cctv(office_copy, r, c, 0, 1, 1, 1)
        dfs(d+1, office_copy)
        office_copy = deepcopy(office)
        apply_cctv(office_copy, r, c, 1, 0, 1, 1)
        dfs(d+1, office_copy)
    elif n == 5:
        apply_cctv(office_copy, r, c, 1, 1, 1, 1)
        dfs(d+1, office_copy)

dfs(0, office)

print(_min)