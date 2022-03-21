from collections import defaultdict
import sys
input=sys.stdin.readline
N, S = map(int, input().split())
seq = list(map(int, input().split()))

dic = defaultdict(int)
for s in seq:
    lst_dic = list(dic.items())
    for i in range(len(lst_dic)):
        dic[lst_dic[i][0]+s] += lst_dic[i][1]
    dic[s] += 1

print(dic[S])