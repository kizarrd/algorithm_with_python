from copy import deepcopy
N, M = map(int, input().split())
lab = []
viruses = []
for i in range(N):
    row = list(map(int, input().split()))
    lab.append(row)
    for j in range(M):
        if row[j] == 2:
            viruses.append((i, j))
lab_default = deepcopy(lab)

moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
def dfs(vr, vc):
    for dr, dc in moves:
        nr, nc = dr+vr, dc+vc
        if 0<=nr<N and 0<=nc<M and lab[nr][nc] == 0:
            lab[nr][nc] = 2
            dfs(nr, nc)

max_safe_area = 0
for w1 in range(N*M):
    if lab[w1//M][w1%M] > 0: continue
    for w2 in range(w1+1, N*M):
        if lab[w2//M][w2%M] > 0: continue
        for w3 in range(w2+1, N*M):
            if lab[w3//M][w3%M] > 0: continue
            lab[w1//M][w1%M], lab[w2//M][w2%M], lab[w3//M][w3%M] = 1, 1, 1
            for vr, vc in viruses:
                dfs(vr, vc)
            # count safe area
            cnt = 0
            for row in lab:
                cnt += row.count(0)
            max_safe_area = max(max_safe_area, cnt)
            # reset lab
            lab = deepcopy(lab_default)

print(max_safe_area)