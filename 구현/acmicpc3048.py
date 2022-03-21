N1, N2 = map(int, input().split())
ants1 = input()[::-1]
ants2 = input()
T = int(input())
a1_positions = [i for i in range(0, len(ants1)*2-1, 2)]
a2_positions = [j for j in range(len(ants1)*2-1, len(ants1)*2+len(ants2)*2, 2)]

answer = [0]*(len(ants1)*2+len(ants2)*2+len(ants1)*2)

if T > len(ants1)+len(ants2):
    T = len(ants1)+len(ants2)
    
for _ in range(T):
    for i in range(len(a1_positions)):
        a1_positions[i] += 2

for p, v in zip(a1_positions, ants1):
    answer[p] = v

for p, v in zip(a2_positions, ants2):
    answer[p] = v

print(''.join(a for a in answer if a!=0))