def solution(n, t, m, p):
    def convert(num, base):
        T = "0123456789ABCDEF"
        result = ''

        while num > 0:
            result = T[num % base] + result  # 나머지를 앞에 추가
            num //= base  # 몫을 다음 숫자로 설정
            
        return result or '0'

    # 전체 단계 구하기
    num = 0
    sequence = ''
    while len(sequence) < t * m:
        sequence += convert(num, n)
        num += 1
    
    # 자기 순서에 맞게 대답하기
    answer = ''
    for i in range(p - 1, t * m, m):
        answer += sequence[i]
    
    return answer
