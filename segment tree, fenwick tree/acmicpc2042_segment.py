# Segment Tree
import sys
input=sys.stdin.readline

N, M, K = map(int, input().split())

A = [int(input()) for _ in range(N)]
tree = [0]*(4*N)

def init(left, right, node):
    if left == right:
        tree[node] = A[left]
        return tree[node]
    mid = (left+right)//2
    tree[node] = init(left, mid, node*2) + init(mid+1, right, node*2+1)
    return tree[node]

# start, end: 세그먼트 트리에서 각 노드가 커버하는 구간의 시작과 끝
# left, right: 구간합을 구하고자 하는 범위
def interval_sum(start, end, node, left, right): 
    # 1. 트리 노드의 구간이 구하고자 하는 구간 밖에 있다면, return 0
    if left > end or right < start:
        return 0
    # 2. 트리 노드의 구간이 구하고자 하는 구간 안에 있다면, return tree[node]
        # 다시, 트리 노드의 구간이 구하고자 하는 구간 안에 있는지 확인하는 것임. 반대가 아님.
    if left <= start and end <= right: 
        return tree[node]
    # 3. 완전 바깥에 있지도 않고, 완전 안에 있지도 않다면, 걸쳐있다는 거니까, 반으로 쪼개서 재귀호출.
    mid = (start+end)//2
    return interval_sum(start, mid, node*2, left, right) + interval_sum(mid+1, end, node*2+1, left, right)

def update(start, end, node, index, diff):
    # 1. 범위 밖이면 종료해야 하니까 리턴.
    if end < index or start > index:
        return
    # 2. 범위 안이면 먼저 해당 트리노드 업데이트 한후, 하위 노드들도 재귀호출로 업데이트.
    tree[node] += diff
    # 2-1. 만약 최하위 노드면 종료해야 하니까 리턴.
    if start == end:
        return
    mid = (start+end)//2
    update(start, mid, node*2, index, diff)
    update(mid+1, end, node*2+1, index, diff)

# 트리 인덱스는 1부터 시작하도록 했지만(계산이 편리함. 왼쪽 자식은 2n, 오른쪽 자식은 2n+1로 나타낼 수 있기 때문), 
# 숫자를 저장한 리스트의 인덱스는 0부터 시작해도 된다.
init(0, N-1, 1)

answers = []
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, N, 1, b, c-A[b-1])
        A[b-1] = c
    else:
        answers.append(interval_sum(1, N, 1, b, c)) # 문제에서 주어진 노드에 매겨진 숫자가 1부터 시작하기 때문에 가능한 것. 0부터 시작한다면 b와 c대신 b+1, c+1을 입력해야 할것.

print(*answers, sep='\n')