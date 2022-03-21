k = int(input())
inequation = input().split()

visited = [0]*10
permutation = []
def dfs(d):
    global _max, _min
    if d == k+1:
        perm_str = ''.join(map(str, permutation))
        if _min == '':
            _min = perm_str
        else:
            _max = perm_str
        return

    for i in range(10):
        if d > 0:
            if not visited[i]:
                visited[i] = 1
                permutation.append(i)
                if (inequation[d-1] == '>' and permutation[d-1] > i) or (inequation[d-1] == '<' and permutation[d-1] < i):
                    dfs(d+1)
                visited[i] = 0
                permutation.pop()
        else:
            if not visited[i]:
                visited[i] = 1
                permutation.append(i)
                dfs(d+1)
                visited[i] = 0
                permutation.pop()

_max = ''
_min = ''
dfs(0)
print(_max)
print(_min)