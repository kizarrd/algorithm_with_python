import math
import sys
input=sys.stdin.readline

T = int(input())
answers = []
for _ in range(T):
    H, _, N = map(int, input().split())
    floor = N%H
    if floor == 0:
        floor = H
    floor = str(floor)
    number = math.ceil(N/H)
    number = str(number)
    if len(number) < 2:
        number = '0'+number
    answers.append(''.join([floor, number]))

print(*answers, sep='\n')