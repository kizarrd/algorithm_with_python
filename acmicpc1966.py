from collections import deque
import sys
input=sys.stdin.readline

answers = []
t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    _input = list(map(int, input().split()))
    documents = deque()
    cnt = 0
    for i, v in enumerate(_input):
        documents.append((i, v))
    while True:
        position, priority = documents.popleft()
        if any(True if x[1] > priority else False for x in documents):
            documents.append((position, priority))
        else:
            cnt += 1
            if position == M:
                answers.append(cnt)
                break

print(*answers, sep='\n')