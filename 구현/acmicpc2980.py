N, L = map(int, input().split())
lights = [list(map(int, input().split())) for _ in range(N)]

prev = 0
t = 0
for D, R, G in lights:
    t += D-prev
    prev = D
    t_cycle = t%(R+G)
    if t_cycle <= R:
        t += R-t_cycle

t += L-lights[-1][0]

print(t)