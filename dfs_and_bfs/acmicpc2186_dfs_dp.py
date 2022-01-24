import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
grid = [input().strip() for _ in range(N)]
word = input().strip()
len_word = len(word)
# visited[r][c][word_idx] = n_paths
visited = [[[-1]*len_word for _ in range(M)] for _ in range(N)]

def dfs(r, c, word_idx):
    cnt = 0

    if visited[r][c][word_idx] > -1:
        return visited[r][c][word_idx]
    if grid[r][c] != word[word_idx]:
        return 0
    if word_idx == len_word-1:
        return 1

    for k in range(1, K+1):
        for dr, dc in ((-k, 0), (0, k), (k, 0), (0, -k)):
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<M:
                cnt += dfs(nr, nc, word_idx+1)

    visited[r][c][word_idx] = cnt
    return cnt

answer = 0
starting_letter = word[0]
for r in range(N):
    for c in range(M):
        if grid[r][c] == starting_letter:
            answer += dfs(r, c, 0)

print(answer)