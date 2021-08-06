import sys
input = sys.stdin.readline

n = 9

heightsList = [int(input()) for _ in range(n)]
heightsList.sort()
sumOfHeights = sum(heightsList)

for i in range(0, n):
    for j in range(i+1, n):
        if sumOfHeights - heightsList[i] - heightsList[j] == 100 :
            for k in range(n):
                if k==i or k==j:
                    continue
                print(heightsList[k])
            sys.exit(0)