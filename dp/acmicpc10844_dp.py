# 0 1 2 3 4 5 6 7 8 9 
#[0 1 1 1 1 1 1 1 1 1]
#[1 1 2 2 2 2 2 2 2 1]
#[1 3 3 4 4 4 4 4 3 2]

N = int(input())
d = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for _ in range(1, N):
    copy = d[:]
    for i in range(len(d)):
        if i == 0:
            d[i] = copy[1]
        elif 0 < i < 9:
            d[i] = copy[i-1]+copy[i+1]
        else:
            d[i] = copy[8]

print(sum(d)%1000000000)