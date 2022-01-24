from collections import deque
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
grid = [input().strip() for _ in range(N)]
word = input().strip()
l_word = len(word)

def bfs(r_start, c_start):
    q = deque()
    q.append((r_start, c_start, 1)) # (row, col, n_letters_found)
    n_paths = 0
    while q:
        r, c, n_letters_found = q.popleft()
        if n_letters_found == l_word:
            n_paths += 1
        else:
            next_letter = word[n_letters_found]
            for k in range(1, K+1):
                for dr, dc in ((-k, 0), (0, k), (k, 0), (0, -k)):
                    nr, nc = r+dr, c+dc
                    if 0<=nr<N and 0<=nc<M and grid[nr][nc] == next_letter:
                        q.append((nr, nc, n_letters_found+1))
    return n_paths

answer = 0
starting_letter = word[0]
for r in range(N):
    for c in range(M):
        if grid[r][c] == starting_letter:
            answer += bfs(r, c)

print(answer)

# 시간초과 발생. DFS + 메모이제이션 으로 풀어야 함. 