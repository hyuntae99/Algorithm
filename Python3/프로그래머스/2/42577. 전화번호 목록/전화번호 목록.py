def solution(phone_book):
    # in 연산자는 set/dict은 O(1), list/tuple은 O(N)
    prefixs = set(phone_book)
    for number in phone_book:
        # 선택한 번호에 대해서 하나씩 증가하며 접두사 생성
        for i in range(1, len(number)):
            prefix = number[:i]
            # 접두사가 있으면 종료
            if prefix in prefixs:
                return False
    return True