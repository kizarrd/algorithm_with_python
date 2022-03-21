from collections import Counter
import sys
input=sys.stdin.readline
N = int(input())
c = Counter()
for _ in range(N):
    c[int(input())] += 1

most_commons = []
most_frequent = c.most_common(1)[0][1]
for key, val in c.most_common():
    if val == most_frequent:
        most_commons.append(key)
    else:
        break

print(min(most_commons))