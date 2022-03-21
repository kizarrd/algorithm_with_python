# Time Limit Exceeded
import sys
input=sys.stdin.readline

T = int(input())
answers = []
for _ in range(T):
    M, N, X, Y = map(int, input().split())
    x, y = 1, 1
    k = 1
    found = False
    while x != M or y != N:
        if x > M:
            x = 1
        if y > N:
            y = 1
        if x == X and y == Y:
            found = True
            break
        x += 1
        y += 1
        k += 1
    
    answers.append(k if found else -1)

print(*answers, sep='\n')