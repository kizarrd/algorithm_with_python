N, M = map(int, input().split())
robot_r, robot_c, robot_dir = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(N)]

moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
cleaned = 0
def move_robot(r, c, robot_dir):
    global cleaned
    if place[r][c] == 0: # if not cleaned,
        place[r][c] = 2 # clean
        cleaned += 1
    
    moved = False
    for i in range(robot_dir+4-1, robot_dir+4-5, -1): # search adjacent cells
        dir = i%4
        dr, dc = moves[dir]
        nr, nc = dr+r, dc+c
        if 0<=nr<N and 0<=nc<M and place[nr][nc] == 0: # if found an uncleaned cell,
            move_robot(nr, nc, dir) # move to that cell
            moved = True
            break
    
    if not moved: # if not found,
        dr, dc = moves[(robot_dir+2)%4]
        nr, nc = dr+r, dc+c
        if 0<=nr<N and 0<=nc<M and place[nr][nc] != 1: # if back is not wall,
            move_robot(nr, nc, robot_dir) # move to back

move_robot(robot_r, robot_c, robot_dir)
print(cleaned)