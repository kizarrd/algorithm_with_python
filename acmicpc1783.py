N, M = map(int, input().split())
'''
항상 오른쪽으로만 이동 가능
세로 길이가 1인 경우: 이동불가(1칸 방문 가능)
세로 길이가 2인 경우: 
    가로 길이가
    1일때: 1칸
    2일때: 1칸
    3이상일 때, 2, 3번 움직임만 가능. 그러니 4번이상 움직일 수 없으므로 4칸 방문이 최대임.
세로 길이가 3이상인 경우: 모든 움직임 다 가능
    하지만 이동 횟수와 방법에 대한 제약을 고려하면.
        가로 길이가 
        2인경우: 2칸. 
        3인경우: 3칸.
        4인경우: 4칸.
        5인경우: 4칸.(제약사항.)
        6인경우: 역시 4칸.
        7 부터: 5칸 이상 가능.(가로길이 7부터는 모든 방법을 한번씩 사용할 수 있게됨.)
        8: 6칸
        9: 7칸
        ...
'''
def cnt(n, m):
    if n == 1:
        return 1
    elif n == 2:
        if m < 3:
            return 1
        else:
            return min(4, 1+(m-1)//2)
    else:
        if m < 4:
            return m
        elif 4 <= m <= 6:
            return 4
        else:
            return m-2

print(cnt(N, M))