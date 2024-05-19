def solution(s):
    answer = 1 # 마지막 문자열은 무조건 혼자이므로
    
    start = s[0]
    cnt = 1
    cnt_else = 0
    for i in s[1:]:
        # 각 카운트가 같아지는 경우
        if cnt == cnt_else:
            answer += 1 
            start = i # 시작 변수 변경
            cnt = 0
            cnt_else = 0
        # 같은 경우
        if i == start:
            cnt += 1
        # 다른 경우
        else:
            cnt_else += 1
    return answer