#이분 그래프
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, depth):
    if depth%2==0:
        visited[x]='A'
    else:
        visited[x]='B'
    for adjacentVertex in adjacencyList[x]:
        if visited[adjacentVertex] == '0':
            dfs(adjacentVertex, depth+1)

def barpitite():
    for j in range(1, v+1):
        for adjv in adjacencyList[j]:
            if visited[j] == visited[adjv]:
                return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    adjacencyList = [[] for _ in range(v+1)]
    visited = ['0']*(v+1)
    for _ in range(e):
        a, b = map(int, input().split())
        adjacencyList[a].append(b)
        adjacencyList[b].append(a)
    for i in range(1, v+1):
        if visited[i] == '0':
            dfs(i, 0)
    print("YES" if barpitite() else "NO")