N, M = map(int, input().split())
lab = []
lab_default = []
viruses = []
n_initial_zeros = 0
for i in range(N):
    row = list(map(int, input().split()))
    n_initial_zeros += row.count(0)
    lab.append(row)
    lab_default.append(row[:])
    for j in range(M):
        if row[j] == 2:
            viruses.append((i, j))

moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
def dfs(vr, vc):
    global cnt
    for dr, dc in moves:
        nr, nc = dr+vr, dc+vc
        if 0<=nr<N and 0<=nc<M and lab[nr][nc] == 0:
            cnt += 1
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
            # count viruses
            cnt = 0
            for vr, vc in viruses:
                dfs(vr, vc)
            safe_area = n_initial_zeros-3-cnt
            max_safe_area = max(max_safe_area, safe_area)
            # reset lab
            for i in range(N):
                lab[i] = lab_default[i][:]

print(max_safe_area)