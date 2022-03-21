E, S, M = map(int, input().split())
if E == 15: E = 0
if M == 19: M = 0
year = S
while True:
    if year%15 == E and year%19 == M:
        print(year)
        exit()
    year += 28