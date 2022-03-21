N = int(input())
S = list(map(int, input().split()))

sums = set()

for elem in S:
    candidates = []
    for s in sums:
        candidates.append(s+elem)
    sums |= set(candidates)
    sums.add(elem)

i = 1
while True:
    if i not in sums:
        print(i)
        exit()
    i+=1