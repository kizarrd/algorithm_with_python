import sys
input=sys.stdin.readline

N = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]

discovered = []
def dfs(v):
  for index, value in enumerate(adj_matrix[v]):
    if value == 1 and index not in discovered:
      discovered.append(index)
      dfs(index)

answer_matrix = [[0]*N for _ in range(N)]

for i in range(N):
  discovered = []
  dfs(i)
  for j in range(N):
    if j in discovered:
      answer_matrix[i][j] = 1

for r in answer_matrix:
  print(*r)