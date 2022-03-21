import sys
input=sys.stdin.readline

T = int(input())
answers = []
for _ in range(T):
    M, N, x, y = map(int, input().split())
    k = x
    answer = -1
    while k < M*N:
        if (k-y)%N == 0:
            answer = k
            break
        k += M
    answers.append(answer)

print(*answers, sep='\n')