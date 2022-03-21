from collections import deque
import sys
input=sys.stdin.readline

N, M, r, c, K = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice_EW = deque([0, 0, 0, 0])
dice_NS = deque([0, 0, 0, 0])

moves = (0, (0, 1), (0, -1), (-1, 0), (1, 0))
for comm in commands:
    dr, dc = moves[comm]
    nr, nc = r+dr, c+dc
    if 0<=nr<N and 0<=nc<M:
        r, c = nr, nc
        if comm == 1:
            dice_EW.rotate(-1)
            if _map[r][c]:
                dice_EW[1] = _map[r][c]
                _map[r][c] = 0
            else:
                _map[r][c] = dice_EW[1]
            dice_NS[1], dice_NS[3] = dice_EW[1], dice_EW[3]
        elif comm == 2:
            dice_EW.rotate(1)
            if _map[r][c]:
                dice_EW[1] = _map[r][c]
                _map[r][c] = 0
            else:
                _map[r][c] = dice_EW[1]
            dice_NS[1], dice_NS[3] = dice_EW[1], dice_EW[3]
        elif comm == 3:
            dice_NS.rotate(-1)
            if _map[r][c]:
                dice_NS[1] = _map[r][c]
                _map[r][c] = 0
            else:
                _map[r][c] = dice_NS[1]
            dice_EW[1], dice_EW[3] = dice_NS[1], dice_NS[3]
        elif comm == 4:
            dice_NS.rotate(1)
            if _map[r][c]:
                dice_NS[1] = _map[r][c]
                _map[r][c] = 0
            else:
                _map[r][c] = dice_NS[1]
            dice_EW[1], dice_EW[3] = dice_NS[1], dice_NS[3]
        
        print(dice_NS[3])