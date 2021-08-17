#스택 수열
n = int(input())

nextNum = 1
stack = []
stack2 = []
for _ in range(n):
    num = int(input())
    if num>=nextNum:
        while num>=nextNum:
            stack.append(nextNum)
            stack2.append('+')
            nextNum+=1
        stack.pop()
        stack2.append('-')
    else:
        while True:
            stack2.append('-')
            if not stack:
                print("NO")
                exit()
            if stack.pop()==num:
                break

for item in stack2:
    print(item)