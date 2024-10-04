def solution(s):
    # 문자열에서 '{', '}' 제거 후, 각각의 튜플을 리스트로 변환
    s = s[2:-2].split('},{')
    # s = s.lstrip('{').rstrip('}').split('},{')
    # 각 튜플의 길이를 기준으로 정렬
    s = sorted(s, key=lambda x: len(x))

    
    answer = []
    # 튜플 내에서 각 숫자를 순서대로 추가 (중복은 제외)
    for group in s:
        numbers = group.split(',')
        for num in numbers:
            if int(num) not in answer:
                answer.append(int(num))
                
    return answer
