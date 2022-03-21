import sys
input=sys.stdin.readline

N = int(input())
requests = list(map(int, input().split()))
budget = int(input())

start = 1
end = max(requests)
limit = 0

while start <= end:
    mid = (start+end)//2

    budgets_distributed = 0
    for req in requests:
        if req <= mid:
            budgets_distributed += req
        else:
            budgets_distributed += mid
    
    if budgets_distributed <= budget:
        limit = mid
        start = mid+1
    else:
        end = mid-1

print(limit)