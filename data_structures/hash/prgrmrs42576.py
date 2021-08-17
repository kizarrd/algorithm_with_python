#완주하지 못한 선수
def solution(participant, completion):
    hash = dict()
    answer=''
    for c in completion:
        if c not in hash:
            hash[c]=1
        else:
            hash[c]+=1

    for p in participant:
        if p not in hash or hash[p]==0:
            answer=p
            break
        else:
            hash[p]-=1

    return answer