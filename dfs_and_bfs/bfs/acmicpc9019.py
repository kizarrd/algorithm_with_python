from collections import deque
import sys
input=sys.stdin.readline
T = int(input())

def bfs(a, b):
    visited = [0]*10001
    q = deque()
    q.append(a) # (n)
    visited[a] = (-1, '')
    while q:
        n = q.popleft()
        # Double
        dn = n*2%10000
        # Subtract
        sn = 0
        if n:
            sn = n-1
        else:
            sn = 9999
        # Left rotate
        ln = (n%1000)*10 + n//1000
        # Right rotate
        rn = (n//10) + (n%10)*1000

        for nn, command in ((dn, 'D'), (sn, 'S'), (ln, 'L'), (rn, 'R')):
            if nn == b:
                answer = command
                prev = n
                while prev != -1:
                    answer += visited[prev][1]
                    prev = visited[prev][0]
                return answer[::-1]

            if not visited[nn]:
                visited[nn] = (n, command)
                q.append(nn)
    return

for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))