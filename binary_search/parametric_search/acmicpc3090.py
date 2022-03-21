import sys
input=sys.stdin.readline

N, T = map(int, input().split())
A = list(map(int, input().split()))

lo, hi = 0, max(A)-min(A)
answer = 0
while lo <= hi:
    mid = (lo+hi)//2
    t = T
    A_copy = A[:]
    ok = True
    for i in range(N-1):
        if (diff:=A_copy[i+1] - A_copy[i]) > mid:
            A_copy[i+1] -= diff-mid
            t -= diff-mid
        if t < 0:
            ok = False
            break
    if ok:
        for i in range(N-1, 0, -1):
            if (diff:=A_copy[i-1] - A_copy[i]) > mid:
                A_copy[i-1] -= diff-mid
                t -= diff-mid
            if t < 0:
                ok = False
                break
    if ok:
        answer = A_copy
        hi = mid-1
    else:
        lo = mid+1

print(*answer)