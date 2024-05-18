def solution(k, m, score):
    answer = 0
    score.sort(reverse = True) # 역순 정렬
    
    # 가장 작은 사과의 점수만 얻기 위한 인덱스
    idx = m - 1
    while True:
        if idx >= len(score):
            break
        # 사과 박스의 가격
        answer += score[idx] * m
        idx += m 
    return answer