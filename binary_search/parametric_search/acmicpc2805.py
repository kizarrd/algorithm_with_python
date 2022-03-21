import sys
input=sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def get_sum_of_lengths_cut_when_H_is(h):
    _sum = 0
    for height in trees:
        if height > h:
            _sum += height - h
    return _sum

answer = 0
def binary_search(start, end):
    global answer
    if start > end:
        return
    mid = (start+end)//2
    _sum = get_sum_of_lengths_cut_when_H_is(mid)
    if _sum == M:
        answer = mid
        return 
    elif _sum < M:
        binary_search(start, mid-1)
    elif _sum > M:
        answer = mid
        binary_search(mid+1, end)

binary_search(0, max(trees))
print(answer)