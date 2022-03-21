import math
from itertools import combinations
N = int(input())
S = [[0]*(N+1)]
for _ in range(N):
    S.append([0]+list(map(int, input().split())))

def get_ability(team):
    total_ability = 0
    for i in range(len(team)):
        for j in range(i, len(team)):
            total_ability += S[team[i]][team[j]]+S[team[j]][team[i]]
    return total_ability

min_gap = math.inf
for team_size in range(1, N//2+1):
    starts = combinations(list(range(1, N+1)), team_size)
    for team_START in starts:
        team_LINK = []
        for player in range(1, N+1):
            if player not in team_START:
                team_LINK.append(player)
        min_gap = min(min_gap, abs(get_ability(team_START) - get_ability(team_LINK)))

print(min_gap)