import sys
input=sys.stdin.readline
N = int(input())
s = list(map(int, input().split()))
inc = [1]*N
dec = [1]*N
for i in range(N):
    longest = 0
    for j in range(i):
        if s[j] < s[i] and inc[j]+1 > longest:
            inc[i] = inc[j]+1
            longest = inc[j]+1
            
longest_bitonic = 0
for i in range(N-1, -1, -1):
    longest = 0
    for j in range(N-1, i, -1):
        if s[j] < s[i] and dec[j]+1 > longest:
            dec[i] = dec[j]+1
            longest = dec[j]+1
    if dec[i]+inc[i]-1 > longest_bitonic:
        longest_bitonic = dec[i]+inc[i]-1

print(longest_bitonic)