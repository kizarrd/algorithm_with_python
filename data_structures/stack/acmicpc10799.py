import sys
input=sys.stdin.readline
given = input().rstrip()

stack = 0
cnt = 0
last = None
for p in given:
    if p == '(':
        stack += 1
    elif p == ')':
        stack -= 1
        if last == '(':
            cnt += stack
        else: # if last == ')':
            cnt += 1
    last = p

print(cnt)