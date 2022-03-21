import sys
input=sys.stdin.readline

DIV = 1000000007

N, M, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
tree = [0]*(4*N)

def init(left, right, node):
    if left == right:
        tree[node] = A[left]
        return tree[node]
    mid = (left+right)//2
    tree[node] = init(left, mid, node*2)*init(mid+1, right, node*2+1)
    return tree[node]%DIV

def update(start, end, node, index, c):
    if end < index or start > index:
        return
    if start == end:
        tree[node] = c
        return
    mid = (start+end)//2
    update(start, mid, node*2, index, c)
    update(mid+1, end, node*2+1, index, c)
    tree[node] = (tree[node*2]*tree[node*2+1])%DIV
    
def interval_product(start, end, node, left, right):
    if start > right or end < left:
        return 1
    if start >= left and end <= right:
        return tree[node]
    mid = (start+end)//2
    return (interval_product(start, mid, node*2, left, right)*interval_product(mid+1, end, node*2+1, left, right))%DIV

init(0, N-1, 1)

answers = []
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, N, 1, b, c)
        A[b-1] = c
    else:
        answers.append(interval_product(1, N, 1, b, c)%DIV)

print(*answers, sep='\n')