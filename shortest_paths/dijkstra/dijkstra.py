from heapq import heappush, heappop
import math

N = None # number of nodes
adj_list = []


def dijkstra(start):
    hq = [(0, start)] # weight first (for heap sorting)
    dist = [math.inf for _ in range(N+1)]
    dist[start] = 0

    while hq:
        w, v = heappop(hq)
        if dist[v] < w: # 뽑을때 확인( <= 하면 처음부터 바로 종료됨)
            continue
        
        for adj_v, adj_w in adj_list[v]:
            alt = w + adj_w
            if alt < dist[adj_v]: # 이부분 중요. 넣을때도 확인.
                dist[adj_v] = alt # 넣기 전에 갱신.
                heappush(hq, (alt, adj_v))

    return dist
