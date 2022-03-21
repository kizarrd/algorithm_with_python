import sys
input = sys.stdin.readline
cursor_left = list(input().rstrip())
cursor_right = []
M = int(input())
for _ in range(M):
    c = input().split()
    if c[0] == 'L' and cursor_left:
        cursor_right.append(cursor_left.pop())
    elif c[0] == 'D' and cursor_right:
        cursor_left.append(cursor_right.pop())
    elif c[0] == 'B' and cursor_left:
        cursor_left.pop()
    elif c[0] == 'P':
        cursor_left.append(c[1])

print(''.join(cursor_left), end='')
print(''.join(cursor_right[::-1]))