import math
N, M = map(int, input().split())
houses = []
chicken_restaurants = []
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            houses.append((r, c))
        elif row[c] == 2:
            chicken_restaurants.append((r, c))

L = len(chicken_restaurants)

def get_city_chicken_distance():
    city_chicken_dist = 0
    for r, c in houses:
        min_chicken_dist = math.inf
        for i in range(L):
            if i not in closed:
                r2, c2 = chicken_restaurants[i]
                chicken_dist = abs(r2-r) + abs(c2-c)
                min_chicken_dist = min(min_chicken_dist, chicken_dist)
        city_chicken_dist += min_chicken_dist
    return city_chicken_dist

_min = math.inf
n_to_be_closed = len(chicken_restaurants)-M
closed = set()
def dfs(d, prev):
    global _min
    if d == n_to_be_closed:
        _min = min(_min, get_city_chicken_distance()) 
        return

    for i in range(prev+1, L):
        closed.add(i)
        dfs(d+1, i)
        closed.remove(i)

dfs(0, -1)

print(_min)