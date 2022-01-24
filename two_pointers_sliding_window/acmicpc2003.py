import sys
input=sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
i, j = 0, 0
sum1 = nums[0]
while i < N and j < N:
    if sum1 < M:
        j += 1
        if j < N: sum1 += nums[j]
    elif sum1 == M:
        cnt += 1
        sum1 -= nums[i]
        i += 1
        j += 1
        if j < N: sum1 += nums[j]
    elif sum1 > M:
        sum1 -= nums[i]
        i += 1

print(cnt)