N, M = map(int, input().split())

def dfs(p, nums):
    if len(nums) == N-M:
        print(p.rstrip())
        return
    
    for i in range(len(nums)):
        n = nums[i]
        np = p+str(n)+' '
        del nums[i]
        n_nums = nums[:]
        dfs(np, n_nums)
        nums.insert(i, n)

dfs('', list(range(1, N+1)))