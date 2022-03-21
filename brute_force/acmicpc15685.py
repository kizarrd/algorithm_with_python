N = int(input())
size = 101
grid = [[0]*size for _ in range(size)]

moves = ((0, 1), (-1, 0), (0, -1), (1, 0))

def mark_dragon_curve(x, y, directions, g):
    if g == 0:
        return
    new_directions = []
    nx, ny = x, y
    for dir in directions[::-1]:
        new_dir = (dir+1)%4
        new_directions.append(new_dir)
        dy, dx = moves[new_dir]
        nx, ny = nx+dx, ny+dy
        grid[ny][nx] = 1

    new_curve = directions + new_directions
    mark_dragon_curve(nx, ny, new_curve, g-1)

# mark each dragon curve
for _ in range(N):
    x, y, d, g = map(int, input().split())
    directions = [d]
    grid[y][x] = 1
    dy, dx = moves[d]
    nx, ny = x+dx, y+dy
    grid[ny][nx] = 1
    mark_dragon_curve(nx, ny, directions, g)

# count squares
cnt = 0
for y in range(size-1):
    for x in range(size-1):
        if all([grid[y][x], grid[y][x+1], grid[y+1][x], grid[y+1][x+1]]):
            cnt += 1

print(cnt)