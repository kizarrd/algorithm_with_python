

n, m, start = map(int, input().split())
vertexList = [ [] for _ in range(n+1) ]
check = [False]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    vertexList[u].append(v)
    vertexList[v].append(u)
for i in range(n):
    vertexList.sort()  

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for adjacentVertex in vertexList[x]:
        if check[adjacentVertex] == False:
            dfs(adjacentVertex)



dfs(start)
print()