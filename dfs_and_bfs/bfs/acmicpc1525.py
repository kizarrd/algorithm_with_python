from collections import deque

Input = [input().split() for _ in range(3)]
first = ''
for row in Input:
    for num in row:
        if num == '0': first += '9'
        else: first += num

dist = {}
q = deque()
q.append((first, 0)) # node, distance

while q:
    n, d = q.popleft()
    if n == '123456789':
        print(d)
        exit()
    dist[n] = d
    # process adjacent nodes
    n_list = list(map(int, n))
    index_9 = n_list.index(9)
    if index_9 > 2:
        n_list_copy = n_list[:]
        n_list_copy[index_9], n_list_copy[index_9-3] = n_list_copy[index_9-3], n_list_copy[index_9]
        adj_n = ''.join(list(map(str, n_list_copy)))
        if adj_n not in dist:
            q.append((adj_n, d+1))
    if index_9%3 < 2:
        n_list_copy = n_list[:]
        n_list_copy[index_9], n_list_copy[index_9+1] = n_list_copy[index_9+1], n_list_copy[index_9]
        adj_n = ''.join(list(map(str, n_list_copy)))
        if adj_n not in dist:
            q.append((adj_n, d+1))
    if index_9 < 6:
        n_list_copy = n_list[:]
        n_list_copy[index_9], n_list_copy[index_9+3] = n_list_copy[index_9+3], n_list_copy[index_9]
        adj_n = ''.join(list(map(str, n_list_copy)))
        if adj_n not in dist:
            q.append((adj_n, d+1))
    if index_9%3 > 0:
        n_list_copy = n_list[:]
        n_list_copy[index_9], n_list_copy[index_9-1] = n_list_copy[index_9-1], n_list_copy[index_9]
        adj_n = ''.join(list(map(str, n_list_copy)))
        if adj_n not in dist:
            q.append((adj_n, d+1))

print(-1)