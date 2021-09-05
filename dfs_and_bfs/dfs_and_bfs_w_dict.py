# adjacency list implemented by a dictionary
# python algorithm interview p323~

# BFS:
# 우선 adjacency list를 dict로 표현한 점과
# 정점의 수만큼 visited나 check list를 만들어 놓고 방문 표시를 해나가는 대신 
# 빈 discovered list에 .append() 방식을 통해 방문하는 순서대로 방문한 정점을 저장해놓는 점이 기존에 내가 정리해 두었던 dfs코드와 다른 점. 

from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

# 1 - 재귀방식
# 1.1 - discovered를 함수 외부에 미리 만들어 놓고 return을 하지 않는 방식

# discovered = []
# def recursive_dfs_a(v):
#     discovered.append(v)
#     for w in graph[v]:
#         if w not in discovered:
#             recursive_dfs_a(w)

# recursive_dfs_a(1)
# print(f'discovered: {discovered}')

# 1.2 - discovered를 함수 인자로 선언하고 return하는 방식. 함수 자체가 discovered list를 리턴하게 됨. 
def recursive_dfs_b(v, discovered = []):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs_b(w, discovered)
    return discovered

print(f'recursive_dfs_b(1): {recursive_dfs_b(1)}')


# 2 - 스택을 이용한 반복구조로 구현
# 보면 얘는 순서가 약간 다른데 인접 정점을 스택에 넣었다가 빼는 과정에서 순서가 거꾸로 되어서 그렇다. 그래도 dfs 맞다. (깊이 우선 맞음. 헷갈리면 p326참고)
def iterative_dfs(start_v):
    discovered = []
    a_stack = [start_v]
    while a_stack:
        v = a_stack.pop()
        if v not in discovered:
            discovered.append(v)
            for end_vertex in graph[v]:
                a_stack.append(end_vertex)
    return discovered

print(f'iterative_dfs(1): {iterative_dfs(1)}')


# BFS - 큐를 이용한 반복 구조로 구현
# 스택을 쓰면 DFS, 큐를 쓰면 BFS가 되는 이유를 이해하자. 
# 파알인은 deque를 안쓰고 그냥 리스트로 pop(0)을 함. 
# dfs랑 비슷하게 graph adjacency list를 dict로 구현한것과 discovered라는 리스트에 append하는 방식이 새로움. 

# BFS는 재귀로 구현하지 못한다고 함. 

def iterative_bfs(start_v):
    discovered = [start_v]
    q = deque()
    q.append(start_v)
    while q:
        v = q.popleft()
        for end_vertex in graph[v]:
            if end_vertex not in discovered:
                discovered.append(end_vertex)
                q.append(end_vertex)
    return discovered

print(f'iterative_bfs(1): {iterative_bfs(1)}')