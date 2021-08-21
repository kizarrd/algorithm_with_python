# 수 묶기
import sys
input = sys.stdin.readline

#양수,양수: 곱하기 
#음수,음수: 곱하기
#수, 1: 더하기
#음수, 0: 곱하기
#양수, 0: 더하기

n = int(input())
positive_int_list = []
negative_int_and_zero_list = []
sum = 0

for _ in range(n):
    new_line = int(input())
    if new_line == 1:
        sum+=1
    elif new_line > 0:
        positive_int_list.append(new_line)
    else:
        negative_int_and_zero_list.append(new_line)

positive_int_list.sort(reverse=True)
negative_int_and_zero_list.sort()

for i, v in enumerate(positive_int_list):
    if i%2==0:
        try:
            sum+=v*positive_int_list[i+1]
        except IndexError:
            sum+=v

for i, v in enumerate(negative_int_and_zero_list):
    if i%2==0:
        try:
            sum+=v*negative_int_and_zero_list[i+1]
        except IndexError:
            sum+=v    

print(sum)