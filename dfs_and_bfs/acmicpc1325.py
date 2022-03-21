from collections import defaultdict, deque
import sys
input=sys.stdin.readline

N, M = map(int, input().split())
adj_list = defaultdict(list)
for _ in range(M):
    c1, c2 = map(int, input().split())
    adj_list[c2].append(c1) # directed from c2 to c1

max_hackable = 0
answers = []
for i in range(1, N+1): # do BFS for all nodes
    q = deque([i])
    visited = [0]*(N+1)
    visited[i] = 1
    cnt_hackable = 0
    while q:
        v = q.popleft()
        cnt_hackable += 1
        for adj_v in adj_list[v]:
            if not visited[adj_v]:
                visited[adj_v] = 1
                q.append(adj_v)
    if cnt_hackable > max_hackable:
        max_hackable = cnt_hackable
        answers = [i]
    elif cnt_hackable == max_hackable:
        answers.append(i)

answers.sort()
print(*answers)