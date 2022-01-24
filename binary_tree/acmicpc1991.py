import sys
input = sys.stdin.readline

class TreeNode:
    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

N = int(input())
trees = {}
while N:
    n, l, r = input().split()
    tl, tr = None, None
    if l != '.':
        tl = TreeNode(l)
        trees[l] = tl
    if r != '.':
        tr = TreeNode(r)
        trees[r] = tr
    
    if n in trees:
        trees[n].left = tl
        trees[n].right = tr
    else:
        trees[n] = TreeNode(n, tl, tr)

    N -= 1

def preorder(key):
    print(key, end='')
    if trees[key].left: preorder(trees[key].left.val)
    if trees[key].right: preorder(trees[key].right.val)

def inorder(key):
    if trees[key].left: inorder(trees[key].left.val)
    print(key, end='')
    if trees[key].right: inorder(trees[key].right.val)

def postorder(key):
    if trees[key].left: postorder(trees[key].left.val)
    if trees[key].right: postorder(trees[key].right.val)
    print(key, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()