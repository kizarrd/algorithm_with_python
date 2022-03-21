N, M = map(int, input().split())
office = []
cctvs = []
for r in range(N):
    row = list(map(int, input().split()))
    office.append(row)
    for c in range(M):
        if 0 < row[c] < 6:
            cctvs.append((row[c], r, c))

cctv_types = [
    0,
    [ [0], [1], [2], [3] ],
    [ [0, 2], [1, 3] ],
    [ [0, 1], [1, 2], [2, 3], [3, 0] ], 
    [ [3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0] ], 
    [ [0, 1, 2, 3] ]
]

moves = ((-1, 0), (0, 1), (1, 0), (0, -1))

def apply_cctv(office, rotation, r, c):
    for dir in rotation:
        dr, dc = moves[dir]
        nr, nc = r+dr, c+dc
        while 0<=nr<N and 0<=nc<M:
            if office[nr][nc] == 6:
                break
            elif office[nr][nc] == 0:
                office[nr][nc] = 7 #
            nr, nc = nr+dr, nc+dc

_min = N*M
def dfs(d, office):
    global _min
    if d == len(cctvs):
        cnt = 0
        for row in office:
            cnt += row.count(0)
        _min = min(_min, cnt)
        return
    
    n, r, c = cctvs[d]
    office_copy = []
    for row in office:
        office_copy.append(row[:])

    for rotations in cctv_types[n]:
        apply_cctv(office_copy, rotations, r, c)
        dfs(d+1, office_copy)
        office_copy = []
        for row in office:
            office_copy.append(row[:])

dfs(0, office)

print(_min)