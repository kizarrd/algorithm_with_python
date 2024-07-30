max_dungeon_visit = 0
visited = []

def dfs(current_fatigue, dungeons, depth=0):
    global max_dungeon_visit
    if depth > max_dungeon_visit:
        max_dungeon_visit = depth
    for i, dungeon in enumerate(dungeons):
        min_fatigue, fatigue_consumption = dungeon
        if current_fatigue >= min_fatigue and not visited[i]:
            visited[i] = 1
            dfs(current_fatigue-fatigue_consumption, dungeons, depth+1)
            visited[i] = 0

def solution(k, dungeons):
    global visited
    visited = [0]*len(dungeons)
    dfs(k, dungeons)
        
    return max_dungeon_visit
