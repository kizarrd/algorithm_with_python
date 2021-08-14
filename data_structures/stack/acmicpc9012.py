#괄호
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    parenthesis_string = list(input().rstrip())
    stack = []
    no = False
    for parenthesis in parenthesis_string:
        if parenthesis=='(':
            stack.append(parenthesis)
        elif parenthesis==')':
            if len(stack)==0:
                no = True
                break
            if stack[-1]=='(':
                stack.pop()

    if no or len(stack)>0:
        print("NO")
    else:
        print("YES")