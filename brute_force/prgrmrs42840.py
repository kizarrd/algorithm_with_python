def solution(answers):
    answer = []
    spj1 = (1, 2, 3, 4, 5)
    spj2 = (2, 1, 2, 3, 2, 4, 2, 5)
    spj3 = (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    spj1_correct = 0
    spj2_correct = 0
    spj3_correct = 0
    
    for i, a in enumerate(answers):
        if spj1[i%5] == a:
            spj1_correct += 1
        if spj2[i%8] == a:
            spj2_correct += 1
        if spj3[i%10] == a:
            spj3_correct += 1
    
    prev = 0
    for c, spj in sorted([(spj1_correct, 1), (spj2_correct, 2), (spj3_correct, 3)], key=lambda x: (x[0], -x[1]), reverse=True):
        if not answer or prev == c:
            answer.append(spj)
            prev = c
    
    return answer