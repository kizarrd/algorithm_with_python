import itertools

def solution(k, dungeons):
    max_dungeon_visit = 0
    paths = list(itertools.permutations(dungeons))
    for path in paths:
        current_fatigue = k
        visit = 0
        for min_fatigue, fatigue_consumption in path:
            if current_fatigue >= min_fatigue:
                visit += 1
                current_fatigue -= fatigue_consumption
                
        if visit > max_dungeon_visit:
            max_dungeon_visit = visit
        
    return max_dungeon_visit