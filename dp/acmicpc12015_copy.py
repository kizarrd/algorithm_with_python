import sys
input=sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

seq = [A[0]]

for i in range(1, N):
    if A[i] > seq[-1]:
        seq.append(A[i])
    else:
        # find lower bound in seq. (find bisect_left)
        low, high = 0, len(seq)
        while low < high: # low == high 일때 종료
            mid = (low+high)//2

            if seq[mid] >= A[i]:
                high = mid
            else:
                low = mid+1

        seq[high] = A[i] # low == high 이므로 low로 해도 됨.

print(len(seq))