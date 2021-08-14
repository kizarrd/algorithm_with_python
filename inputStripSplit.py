import sys
input = sys.stdin.readline

stringList_wo_split = list(input())

stringList_w_strip = list(input().strip())

stringList_w_split = list(input().split())

stringList_w_strip_split = list(input().strip().split())

print(stringList_wo_split, stringList_w_strip, stringList_w_split, stringList_w_strip_split)

# input:
# 12345
# 12345
# 1 2 3 4 5 
# 1 2 3 4 5