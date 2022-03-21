N, M = map(int, input().split())
rect = [list(map(int, input())) for _ in range(N)]

_max = 0
if M >= 3:
    for i in range(0, M-2):  
        for j in range(i+1, M-1):
            r1, r2, r3 = 0, 0, 0
            for r in range(0, N):
                for c in range(0, i+1): r1 += rect[r][c]
                for c in range(i+1, j+1): r2 += rect[r][c]
                for c in range(j+1, M): r3 += rect[r][c]
            _max = max(_max, r1*r2*r3)
if N >= 3:
    for i in range(0, N-2):  
        for j in range(i+1, N-1):
            r1, r2, r3 = 0, 0, 0
            for r in range(0, i+1): r1 += sum(rect[r])
            for r in range(i+1, j+1): r2 += sum(rect[r])
            for r in range(j+1, N): r3 += sum(rect[r])
            _max = max(_max, r1*r2*r3)

if N >= 2 and M >= 2:
    for i in range(0, N-1):
        for j in range(0, M-1):
            r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            for c in range(0, j+1):
                for r in range(0, i+1): r1 += rect[r][c]
                for r in range(i+1, N): r2 += rect[r][c]
            for r in range(0, N):
                for c in range(j+1, M): r3 += rect[r][c]
                for c in range(0, j+1): r6 += rect[r][c]

            for c in range(j+1, M):
                for r in range(0, i+1): r4 += rect[r][c]
                for r in range(i+1, N): r5 += rect[r][c]
            
            for r in range(i+1, N):
                for c in range(0, j+1): r8 += rect[r][c]
                for c in range(j+1, M): r9 += rect[r][c]
                for c in range(0, M): r12 += rect[r][c]
            
            for r in range(0, i+1):
                for c in range(0, M): r7 += rect[r][c]
                for c in range(0, j+1): r10 += rect[r][c]
                for c in range(j+1, M): r11 += rect[r][c]
            
            _max = max(_max, r1*r2*r3, r4*r5*r6, r7*r8*r9, r10*r11*r12)

print(_max)