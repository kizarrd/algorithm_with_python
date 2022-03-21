import sys
input=sys.stdin.readline

n, k = map(int, input().split())
events = [[0]*(n+1) for _ in range(n+1)] 
# events[i][j] 가 1이면 i가 j보다 먼저 일어났음을 뜻한다. 0이면 알 수 없음을 뜻한다.

for _ in range(k):
    a, b = map(int, input().split())
    events[a][b] = 1

# floyd-warshall
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # i가 k보다 먼저 일어나고, k가 j보다 먼저 일어났다면,
            # i가 j보다 먼저 일어난 것이다.
            if events[i][k] and events[k][j]:
                events[i][j] = 1

s = int(input())
answers = []
for _ in range(s):
    a, b = map(int, input().split())
    if events[a][b]:
        answers.append(-1)
    elif events[b][a]:
        answers.append(1)
    else:
        answers.append(0)

print(*answers, sep='\n')