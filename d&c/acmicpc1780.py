import sys
input=sys.stdin.readline
N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]

def check_all_same(p):
    num = p[0][0]
    for row in p:
        for e in row:
            if e != num:
                return False
    return True

def count(p):
    len_p = len(p)
    if check_all_same(p):
        cnt[p[0][0]] += 1
        return

    for r in range(3):
        for c in range(3):
            cut_papers = []
            len_cut_p = len_p//3
            for nr in range(r*len_cut_p, (r+1)*len_cut_p):
                cut_papers.append(p[nr][c*len_cut_p:(c+1)*len_cut_p])
            count(cut_papers)

cnt = { -1: 0, 0: 0, 1: 0}
count(p)
print(cnt[-1], cnt[0], cnt[1], sep='\n')