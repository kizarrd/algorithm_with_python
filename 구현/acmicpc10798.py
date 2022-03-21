import sys
input=sys.stdin.readline
words = [list(input().rstrip()) for _ in range(5)]

answer = ''
max_c = max(len(w) for w in words)
for c in range(max_c):
    for r in range(5):
        if c < len(words[r]):
            answer += words[r][c]

print(answer)