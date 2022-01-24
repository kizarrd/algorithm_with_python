from collections import deque

F, S, G, U, D = map(int, input().split())

dist = {}
q = deque()
q.append(S)
dist[S] = 0
while q:
    f = q.popleft()
    for move in (U, -D):
        next_f = f+move
        if 1 <= next_f <= F and next_f not in dist:
            dist[next_f] = dist[f]+1
            q.append(next_f)

if G in dist:
    print(dist[G])
else:
    print("use the stairs")