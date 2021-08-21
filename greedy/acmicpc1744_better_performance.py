import sys
input = sys.stdin.readline

n = int(input())
seq = []
for i in range(n):
    seq.append(int(input()))

pos = []
neg = []
answer = 0

for i in seq:
    if i == 1:
        answer += i
    elif i > 0:
        pos.append(i)
    else:
        neg.append(i)
        

pos.sort(reverse = True)
neg.sort()

for i in range(0, len(pos), 2):
    if i < len(pos) - 1:
        answer += pos[i] * pos[i+1]
    else:
        answer += pos[i]
        
for i in range(0, len(neg), 2):
    if i < len(neg) - 1:
        answer += neg[i] * neg[i+1]
    else:
        answer += neg[i]
        
    
print(answer)