#전화번호 목록 문제
def solution(phone_book):
    answer = True
    
    for phone_number in phone_book:
        phone_number_len = len(phone_number)
        for phone_number2 in phone_book:
            if phone_number==phone_number2:
                continue
            try:
                if phone_number2[:phone_number_len] == phone_number:
                    answer = False
                    return answer            
            except IndexError:
                continue
                
    return answer

#정확성 테스트는 통과했으나 효율성 테스트에서 실패함. (시간초과)
#해시를 안썼기 때문에 당연한 결과