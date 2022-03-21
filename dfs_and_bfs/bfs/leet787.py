from collections import deque
import math
class Solution:
    def __init__(self):
        self.a = None

    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        adj_list = [list() for _ in range(n)]
        for f, t, p in flights:
            adj_list[f].append((t, p))
        
        q = deque()
        q.append((src, 0, 0)) # node, price, stops
        cost = [math.inf]*n
        while q:
            v, p, s = q.popleft()
            if s == k+1 or v == dst:
                continue
            for adj_v, adj_p in adj_list[v]:
                if p + adj_p < cost[adj_v]:
                    cost[adj_v] = p + adj_p
                    q.append((adj_v, p + adj_p, s+1))
        
        return cost[dst] if cost[dst] < math.inf else -1

s = Solution()
print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))