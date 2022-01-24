from bisect import bisect, insort
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr_sorted = sorted(arr)

cnt = 0
position_stack = []
for i in range(N-1, -1, -1):
    max_current = arr_sorted[i]
    position_before_sort = arr.index(max_current)
    n_greater_nums_on_left = bisect(position_stack, position_before_sort)
    if position_before_sort-n_greater_nums_on_left < i:
        cnt += i-position_before_sort + n_greater_nums_on_left
    insort(position_stack, position_before_sort)

print(cnt)

# time limit exceeded