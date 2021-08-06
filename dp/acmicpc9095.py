import sys
input = sys.stdin.readline

# we know that d.1 = 1, d.2 = 2, d.3 = 4
# the rule is that d.n = d.(n-1) + d.(n-2) + d.(n-3)

memo = [1, 2, 4]

test_cases = int(input())

for i in range(test_cases):
    n = int(input())
    if n-1<len(memo):
        print(memo[n-1])
    else:
        for j in range(3, n):
            if j>=len(memo):
                memo.append(memo[j-3]+memo[j-2]+memo[j-1])
        print(memo[-1])