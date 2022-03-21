from heapq import heappush, heappop
import sys
input=sys.stdin.readline

moves = ((-1, 0), (0, 1), (1, 0), (0, -1))

i = 1
answers = []
while True:
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    hq = [(cave[0][0], 0, 0)] # w, r, c

    while hq:
        w, r, c = heappop(hq)
        if dist[r][c] == -1:
            if r == N-1 == c:
                answers.append(f'Problem {i}: {w}')
                break
            dist[r][c] = w
            for dr, dc in moves:
                nr, nc = r+dr, c+dc
                if 0<=nr<N and 0<=nc<N:
                    heappush(hq, (cave[nr][nc]+w, nr, nc))
    
    i += 1

print(*answers, sep='\n')