def solution(sequence, target):
    start, end = 0, 0
    current_sum = sequence[0]
    min_length = float('inf')  # 최소 길이를 추적할 변수
    answer = []

    while end < len(sequence):
        if current_sum == target:
            # 현재 부분 수열의 길이가 최소일 때 정답 갱신
            if end - start < min_length:
                min_length = end - start
                answer = [start, end]
            # target을 찾은 후 start를 이동시켜 새로운 부분 수열 찾기
            current_sum -= sequence[start]
            start += 1
        elif current_sum < target:
            # 합이 target보다 작으면 end 포인터 증가
            end += 1
            if end < len(sequence):
                current_sum += sequence[end]
        else:
            # 합이 target보다 크면 start 포인터 증가
            current_sum -= sequence[start]
            start += 1
    
    return answer
