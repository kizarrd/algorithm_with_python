import sys
input=sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    a_and_b = [list(map(int, input().split())) for _ in range(M)]
    a_and_b.sort(key=lambda x: x[1])
    taken = [0]*(1+N)
    cnt = 0
    for a, b in a_and_b:
        for i in range(a, b+1):
            if not taken[i]:
                taken[i] = 1
                cnt += 1
                break
    print(cnt)