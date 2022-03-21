S = input()
alpha_counter = [0]*(ord('z')-ord('a')+1)
shift = ord('a')
for s in S:
    alpha_counter[ord(s)-shift] = S.count(s)
print(*alpha_counter)