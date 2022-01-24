# first: 1~9
# last: 0~9

N = int(input())
answer = [0]
def dfs(i, prev=None):
    if i == 0:
        for n_first in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            dfs(i+1, n_first)
    elif i == N:
        answer[0] += 1
    else:
        if prev > 0:
            dfs(i+1, prev-1)
        if prev < 9:
            dfs(i+1, prev+1)
dfs(0)
print(answer[0])

# time limit exceeded