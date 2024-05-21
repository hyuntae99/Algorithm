def solution(n):
    answer = 0
    for i in range(1, n + 1):
        curr_sum = 0 
        start = i 
        # 시작 정수부터 연속된 수를 더한다.
        while curr_sum < n:
            curr_sum += start  
            start += 1
        # 표현이 가능하면 카운트
        if curr_sum == n:
            answer += 1
    return answer