N = int(input())
positives = []
negatives = []
for _ in range(N):
    n = int(input())
    if n > 0: positives.append(n)
    else: negatives.append(n)

positives.sort(reverse=True)
negatives.sort()
answer = 0

if len(positives)%2 == 1:
    answer += positives[-1]
    bound = len(positives)-2
else:
    bound = len(positives)-1
for i in range(0, bound, 2):
    n1, n2 = positives[i], positives[i+1]
    if n1 > 1 and n2 > 1:
        answer += n1*n2
    else:
        answer += n1+n2

if len(negatives)%2 == 1:
    answer += negatives[-1]
    bound = len(negatives)-2
else:
    bound = len(negatives)-1
for i in range(0, bound, 2):
    n1, n2 = negatives[i], negatives[i+1]
    answer += n1*n2

print(answer)