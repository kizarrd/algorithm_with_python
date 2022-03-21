import sys
input=sys.stdin.readline

A = ' '+input().rstrip()
B = ' '+input().rstrip()

dp = [['']*(len(B)+1) for _ in range(len(A)+1)]
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1]+A[i]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=lambda x: len(x))

LCS = dp[len(A)-1][len(B)-1]
print(len(LCS))
if len(LCS): 
    print(LCS)