from collections import deque

N, M = map(int, input().split())
board = []
R, B = None, None
for i in range(N):
    row = input()
    board.append(list(row))
    if (fr:=row.find('R')) > -1: R = (i, fr)
    if (fb:=row.find('B')) > -1: B = (i, fb)

def noBlue_inFrontOf_red(dr, dc, rR, cR, rB, cB):
    nr, nc = dr+rR, dc+cR
    while True:
        if nr==rB and nc==cB:
            return False
        elif board[nr][nc] == '#' or board[nr][nc] == 'O':
            return True
        nr += dr
        nc += dc

def simulateBlue(dr, dc, rB, cB, rR, cR):
    nr, nc = dr+rB, dc+cB
    while True:
        if board[nr][nc] == 'O':
            return (-1, -1)
        if board[nr][nc] == '#' or (nr==rR and nc==cR):
            return (nr-dr, nc-dc)
        nr += dr
        nc += dc

def simulateRed(dr, dc, rR, cR, rB, cB):
    nr, nc = dr+rR, dc+cR
    while True:
        if board[nr][nc] == 'O':
            return (-1, -1)
        if board[nr][nc] == '#' or (nr==rB and nc==cB):
            return (nr-dr, nc-dc)
        nr += dr
        nc += dc
        
moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
visited = [[set() for _ in range(M)] for _ in range(N)]
q = deque()
q.append((R[0], R[1], B[0], B[1], 0)) # row R, column R, row B, columnm B, number of moves
visited[R[0]][R[1]].add((B[0], B[1]))

while q:
    rR, cR, rB, cB, n = q.popleft()

    for i in range(4):
        dr, dc = moves[i]
        nrR, ncR, nrB, ncB = None, None, None, None

        if noBlue_inFrontOf_red(dr, dc, rR, cR, rB, cB):
            nrR, ncR = simulateRed(dr, dc, rR, cR, rB, cB)
            nrB, ncB = simulateBlue(dr, dc, rB, cB, nrR, ncR)
            if nrB == -1: continue
        else:
            nrB, ncB = simulateBlue(dr, dc, rB, cB, rR, cR)
            if nrB == -1: continue
            nrR, ncR = simulateRed(dr, dc, rR, cR, nrB, ncB)

        if (nrB, ncB) not in visited[nrR][ncR]:
            if nrR == -1:
                print(n+1)
                exit()
            
            visited[nrR][ncR].add((nrB, ncB))
            if (n+1) < 10:
                q.append((nrR, ncR, nrB, ncB, n+1))

print(-1)