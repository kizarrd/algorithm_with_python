import sys
input=sys.stdin.readline

N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]

lo = 1
hi = M*max(T)
answer = 0

while lo <= hi:
    mid = (lo+hi)//2

    n_passed = 0
    for t in T:
        n_passed += mid//t

    if n_passed >= M:
        answer = mid
        hi = mid-1
    else:
        lo = mid+1

print(answer)