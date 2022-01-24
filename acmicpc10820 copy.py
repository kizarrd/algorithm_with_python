import sys
input=sys.stdin.readline

while True:
    string = input().rstrip('\n')
    if not string:
        break    

    lo, up, num, space = 0, 0, 0, 0

    for chr in string:
        if chr.islower(): lo += 1
        elif chr.isupper(): up += 1
        elif chr.isdigit(): num += 1
        else: space += 1
    
    print(lo, up, num, space)