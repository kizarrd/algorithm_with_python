import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

N = int(input())
W = int(input())
cases = [0] + [list(map(int, input().split())) for _ in range(W)]

'''
dp[i][j] = 경찰차1이 마지막으로 처리한 사건이 i번째 사건, 경찰차2가 마지막으로 처리한 사건이 j번째 사건일때, 남은 이동거리의 최솟값.
즉 우리가 찾는 답은 dp[0][0].

answers[i][j] = 경찰차1이 마지막으로 처리한 사건이 i번째 사건, 경찰차2가 마지막으로 처리한 사건이 j번째 사건일때, 실제로 움직였던 경찰차의 번호
'''
dp = [[-1]*(W+1) for _ in range(W+1)]
answers = [[0]*(W+1) for _ in range(W+1)]

def get_distance(_from, _to):
    r1, c1 = _from
    r2, c2 = _to
    return abs(r2-r1)+abs(c2-c1)

def get_dp(i, j):
    if i == W or j == W: # 마지막 사건을 처리했다면 더이상 이동거리는 없으므로 0을 리턴
        return 0
    
    if dp[i][j] != -1: # 이미 계산한 값이라면 리턴. (메모이제이션이 효과를 발휘하는 부분)
        return dp[i][j]

    next_case = max(i, j) + 1
    position_1 = cases[i] if i > 0 else [1, 1] # [0, 0] 으로 했다가 틀렸다.
    position_2 = cases[j] if j > 0 else [N, N]
    distance_1 = get_dp(next_case, j) + get_distance(position_1, cases[next_case]) # 1번 경찰차를 출동시키는 경우
    distance_2 = get_dp(i, next_case) + get_distance(position_2, cases[next_case]) # 2번 경찰차를 출동시키는 경우

    if distance_1 < distance_2:
        answers[i][j] = 1
    else:
        answers[i][j] = 2
    
    dp[i][j] = min(distance_1, distance_2)
    return dp[i][j]

print(get_dp(0, 0))
# get car numbers
i, j = 0, 0
while max(i, j) < W: # 여기도 while 조건이랑 
    car = answers[i][j]
    print(car)
    if car == 1:
        i = max(i, j)+1 # 이부분 어려웠다. 다음 사건은 max(i, j)+1이라는 것을 명심하자.
    else:
        j = max(i, j)+1