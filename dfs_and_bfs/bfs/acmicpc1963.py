from collections import deque

T = int(input())
testcases = [list(map(int, input().strip().split())) for _ in range(T)]
# get prime numbers
limit = 10000
primes = [True]*limit
primes[0], primes[1] = False, False
for i in range(2, int(limit**0.5)):
    if primes[i]:
        multiplier = 2
        while i*multiplier < limit:
            primes[i*multiplier] = False
            multiplier += 1

def bfs(start, end):
    dist = {}
    q = deque()
    q.append(start)
    dist[start] = 0

    while q:
        node = q.popleft()
        if node == end:
            return dist[node]
        for tens in (1, 10, 100, 1000):
            upper_bound = ((node//(tens*10))+1)*(tens*10)
            lower_bound = 999 if tens == 1000 else (node//(tens*10))*(tens*10)-1
            next = node+tens
            while next < upper_bound:
                if primes[next] and next not in dist: 
                    q.append(next)
                    dist[next] = dist[node]+1
                next+=tens
            next = node-tens
            while next > lower_bound:
                if primes[next] and next not in dist: 
                    q.append(next)
                    dist[next] = dist[node]+1
                next-=tens
    
    return 'Impossible'

for start, end in testcases:
    print(bfs(start, end))