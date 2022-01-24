from collections import deque

puzzle = [input().split() for _ in range(3)]
first = ''
for row in puzzle:
    first += ''.join(row)

dist = {}
q = deque()
q.append(first) # node, distance
dist[first] = 0
while q:
    n = q.popleft()
    if n == '123456780':
        print(dist[n])
        exit()
    # process adjacent nodes
    index_zero = n.index('0')
    r, c = index_zero//3, index_zero%3
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr, nc = r+dr, c+dc
        if -1<nr<3 and -1<nc<3:
            n_list = list(n)
            i = nr*3+nc
            n_list[i], n_list[index_zero] = n_list[index_zero], n_list[i]
            n_num = ''.join(n_list)
            if n_num not in dist:
                dist[n_num] = dist[n]+1
                q.append(n_num)

print(-1)