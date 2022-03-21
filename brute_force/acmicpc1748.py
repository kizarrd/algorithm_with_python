'''
1 => 1~9: 9
10 => 10~99: 90
100 => 100~999: 900
'''
N = int(input())
arr = [0]+[9*(10**i) for i in range(9)]
answer = 0

for i in range(1, len(str(N))):
    answer += arr[i]*i

last_power_of_ten = 10**(len(str(N))-1)
answer += (N-(last_power_of_ten-1))*len(str(N))
print(answer)