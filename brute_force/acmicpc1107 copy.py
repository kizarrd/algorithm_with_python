import math
N = int(input())
M = int(input())
brokens = []
if M > 0:
    brokens = input().split()

prev_min = math.inf
for i in range(0, 10**6):
    possible_channel = True
    for each_b in brokens:
        if each_b in str(i):
            possible_channel = False
            break
    if possible_channel and abs(N-i)+len(str(i)) < prev_min:
        prev_min = abs(N-i)+len(str(i))

print(min(abs(N-100), prev_min))