import sys
input=sys.stdin.readline

T = int(input())
answers = []

def get_answer(a, b, m, n):
    answer = -1
    k = a
    while k < m*n:
        if (k-b)%n == 0:
            answer = k
            break
        k += m
    return answer

for _ in range(T):
    M, N, x, y = map(int, input().split())
    k = x
    a = x if M >= N else y
    b = x if M < N else y
    print(get_answer(a, b, max(M, N), min(M, N)))