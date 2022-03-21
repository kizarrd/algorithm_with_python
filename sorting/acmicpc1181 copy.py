import sys
input=sys.stdin.readline
N = int(input())
words = [input().rstrip() for _ in range(N)]
words.sort(key=lambda x: (len(x), x))
prev = ''
for word in words:
    if word != prev:
        print(word)
    prev = word