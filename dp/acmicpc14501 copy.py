N = int(input())
T, P = [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# d[i] = i번째 날부터 일을 시작했을때 얻을 수 있는 최대 수익
d = [0]*(N+2) # 아래 루프에서 i=N일때를 포함하기 위해 N+1까지의 인덱스가 필요함
for i in range(N, 0, -1):
    if T[i] > N-i+1: # i번째날에 잡혀있는 상담을 끝마칠 수 없는 경우,
        d[i] = d[i+1] # i번째날의 상담은 포기할 수밖에 없다. 
    else: # 끝마칠 수 있는 경우,
        d[i] = max(P[i]+d[i+T[i]], d[i+1]) # i번째날의 상담을 하는 경우와 하지 않는 경우 중 수익이 최대인 것을 선택

print(d[1]) # 첫번째 날부터 일을 시작했을때 얻을 수 있는 최대 수익