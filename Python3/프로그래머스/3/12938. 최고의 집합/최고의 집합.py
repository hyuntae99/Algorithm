def solution(n, s):
    # 예외 처리: n이 s보다 클 경우 불가능
    if n > s:
        return [-1]
    
    # s를 n으로 나눈 몫과 나머지 계산
    q = s // n
    r = s % n
    
    # 결과 배열 생성 -> 균등하게 배분하는 것이 가장 곱셈이 크다!!
    result = [q] * n
    
    # 나머지 r만큼 각 요소에 1씩 더해줌
    for i in range(r):
        result[i] += 1
    
    # 오름차순 정렬
    result.sort()
    
    return result
