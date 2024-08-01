import collections

adj_list = collections.defaultdict(list)
visited = []

def dfs(v1, except_v1, except_v2):
    visited[v1] = 1
    for v2 in adj_list[v1]:
        if (v1 == except_v1 and v2 == except_v2) or (v1 == except_v2 and v2 == except_v1):
            continue
        if visited[v2] == 0:
            dfs(v2, except_v1, except_v2)

def solution(n, wires):
    global adj_list, visited
    for v1, v2 in wires:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
    
    min_diff = n
    visited = [0]*(n+1)
    for v1, v2 in wires:
        dfs(v1, v1, v2)
        diff = abs(sum(visited) - (n - sum(visited)))
        if diff < min_diff:
            min_diff = diff
        visited = [0]*(n+1)
        
    return min_diff