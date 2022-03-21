import sys
input=sys.stdin.readline

n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# triangle[i][j] = max sum if [i][j] is the last number of the path
for i in range(1, n):
    for j in range(i+1):
        candidates = []
        if j-1 >= 0: candidates.append(triangle[i-1][j-1])
        if j < i: candidates.append(triangle[i-1][j])
        triangle[i][j] += max(candidates)

print(max(triangle[n-1]))