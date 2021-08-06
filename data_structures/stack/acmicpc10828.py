#only if and elif
import sys
input=sys.stdin.readline

stack = []

for i in range(int(input())):
    list = input().strip().split()
    if len(list)==2:
        a, b = list
    else:
        a = list[0]
    if a=="push":
        stack.append(int(b))
    elif a=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif a=="size":
        print(len(stack))
    elif a=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif a=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])