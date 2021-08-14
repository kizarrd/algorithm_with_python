#덩치
import sys
input = sys.stdin.readline

n = int(input())
people = [ list(map(int, input().split())) for _ in range(n)]

for person in people:
    ranking = 1
    for otherPerson in people:
        if person != otherPerson:
            if otherPerson[0] > person[0] and otherPerson[1] > person[1]:
                ranking += 1
    print(ranking, end=' ')