import sys
input=sys.stdin.readline
K, S, N = input().split() # King, Stone, N
alpha = '0ABCDEFGH'
cK, rK = alpha.index(K[0]), int(K[1]) # column King, row King
cS, rS = alpha.index(S[0]), int(S[1])

moves = {
    'R': (1, 0),
    'L': (-1, 0),
    'B': (0, -1),
    'T': (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1)
}

for _ in range(int(N)):
    m = input().rstrip()
    dc, dr = moves[m]
    ncK, nrK = cK+dc, rK+dr
    if ncK == cS and nrK == rS:
        if 1<=cS+dc<=8 and 1<=rS+dr<=8:
            cK, rK = ncK, nrK
            cS, rS = cS+dc, rS+dr
    elif 1<=ncK<=8 and 1<=nrK<=8:
        cK, rK = ncK, nrK

print(alpha[cK], rK, sep='')
print(alpha[cS], rS, sep='')