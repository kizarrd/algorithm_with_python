from bisect import bisect_left
N = input()
M = int(input())
buttons = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
if M > 0:
    buttons -= set(list(map(int, (input().split()))))
buttons = list(buttons)
buttons.sort()
if int(N) == 0:
    if buttons:
        print(buttons[0]+1)
    else:
        print(100)
    exit()
if 97 <= int(N) <= 103 or not buttons:
    print(abs(int(N)-100))
    exit()

answers = []
stack = []

if len(N) > 1:
    stack.append((1, -1, '0'))
if buttons[0] > 0:
    stack.append((0, 1, str(buttons[0])))
elif len(buttons) > 1:
    stack.append((0, 1, str(buttons[1])))
    
stack.append((0, 0, ''))
while stack:
    i, prev, a = stack.pop()
    # print(a)
    if i == len(N):
        answers.append(a)
        # print(answers)
    else:
        if prev == 1:
            b = a+str(buttons[0])
            stack.append((i+1, 1, b))
        elif prev == -1:
            b = a+str(buttons[-1])
            stack.append((i+1, -1, b))
        elif prev == 0:
            n = bisect_left(buttons, int(N[i]))
            if n == len(buttons):
                b = a+str(buttons[-1])
                stack.append((i+1, -1, b))
            elif buttons[n] == int(N[i]):
                b = a+str(buttons[n])
                stack.append((i+1, 0, b))
                if n+1 < len(buttons):
                    b = a+str(buttons[n+1])
                    stack.append((i+1, 1, b))
                if n-1 >= 0:
                    b = a+str(buttons[n-1])
                    stack.append((i+1, -1, b))
            elif n == 0:
                b = a+str(buttons[n])
                stack.append((i+1, 1, b))
            elif buttons[n] > int(N[i]):
                b = a+str(buttons[n])
                stack.append((i+1, 1, b))
                b = a+str(buttons[n-1])
                stack.append((i+1, -1, b))

# print(answers)
cnt = min(map(lambda x: len(str(int(x)))+abs(int(x)-int(N)), answers))
print(min(cnt, abs(int(N)-100)))