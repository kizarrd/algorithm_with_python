import sys
input=sys.stdin.readline
T = int(input())
for _ in range(T):
    _input = input().rstrip()
    d = [0]*len(_input)
    d[0] = 1 if _input[0]=='O' else 0
    if len(_input) == 1:
        print(d[0])
        continue
    
    for i in range(1, len(_input)):
        if _input[i] == 'O':
            d[i] = 1
            if _input[i-1] == 'O':
                d[i] += d[i-1]

    print(sum(d))