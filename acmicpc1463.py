N = int(input())
d = [0]*(N+1)
'''
d[2] = 1
d[3] = 1
d[4] = d[4//2]+1 = d[4-1]+1 = 2
d[5] = 
'''
for i in range(2, N+1):
    candidates = []
    if i%3 == 0: candidates.append(d[i//3]+1)
    if i%2 == 0: candidates.append(d[i//2]+1)
    candidates.append(d[i-1]+1)
    d[i] = min(candidates)

print(d[N])