N, M = map(int, input().split())
rect = [list(map(int, input())) for _ in range(N)]

initial_width = min(N, M)
for w in range(initial_width, 0, -1):
    for r in range(N-w+1):
        for c in range(M-w+1):
            if rect[r][c] == rect[r][c+w-1] == rect[r+w-1][c+w-1] == rect[r+w-1][c]:
                print(w*w)
                exit()