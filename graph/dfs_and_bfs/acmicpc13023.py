N, M = map(int, input().split())
people = [[] for _ in range(N)]
check = [False]*N

for _ in range(M):
    u, v = map(int, input().split())
    people[u].append(v)
    people[v].append(u)

def dfs(x, depth):
    if depth == 4:
        print(1)
        exit()
    for friend in people[x]:
        if check[friend] == False:
            check[x] = True
            dfs(friend, depth+1)
            check[x] = False

for person in range(N):
    check[person] = True
    dfs(person, 0)
    check[person] = False

print(0)