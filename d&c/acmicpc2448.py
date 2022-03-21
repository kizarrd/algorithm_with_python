# 비효율적인 나의 최초 솔루션
N = int(input())
pattern = [[' ']*(N*2-1) for _ in range(N)]

next_triangle = "** ******"
middle = (N*2-1)//2
pattern[0][middle] = '*'
for i in range(1, 4): pattern[1][middle-2+i] = next_triangle[i]
for i in range(4, 9): pattern[2][middle-6+i] = next_triangle[i]

left, right = (N*2-1)//2-3, (N*2-1)//2+3
i = 6
while i <= N:
    width = 1
    c1, c2 = left, right
    i_triangle = 0
    for r in range(i//2, i):
        for dc in range(width):
            nc1, nc2 = c1+dc, c2+dc
            pattern[r][nc1] = pattern[r][nc2] = next_triangle[i_triangle+dc]

        next_triangle += ''.join(pattern[r][c1:c2+width])
        c1, c2 = c1-1, c2-1
        i_triangle += width
        width += 2

    left, right = c1, (c2+1)+(width-2)
    i*=2

for row in pattern:
    print(''.join(row))