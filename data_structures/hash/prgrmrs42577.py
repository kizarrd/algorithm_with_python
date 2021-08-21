#전화번호 목록 문제
def solution(phone_book):
    answer = True

    phone_number_hash = {}

    for phone_number in phone_book:
        phone_number_len = len(phone_number)
        for i in range(1, phone_number_len):
            phone_number_hash[phone_number[:i]]=1
    for phone_number2 in phone_book:
        if phone_number2 in phone_number_hash:
            answer=False
            break

    return answer