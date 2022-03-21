N = [0]+list(map(int, input()))
n = len(N)
d = [0]*n # d[i] = 0번째까지로 된 암호가 해석될 수 있는 경우의 수
d[0], d[1] = 1, 1

if N[1] == 0:
    print(0)
    exit()

for i in range(2, n):
    if N[i] != 0:
        if N[i-1] != 0 and N[i-1]*10+N[i] <= 26:
            d[i] = d[i-2]+d[i-1]
        else:
            d[i] = d[i-1]
    else: # if N[i] == 0:
        if N[i-1] != 0 and N[i-1]*10+N[i] <= 26:
            d[i] = d[i-2]
        else:
            print(0)
            exit()

print(d[n-1]%1000000)