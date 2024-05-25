def solution(n, times):
    # 최소 시간은 1분
    left = 1
    # 최대 시간은 가장 느린 검사관이 모든 사람을 검사할 때 걸리는 시간
    right = max(times) * n
    
    # 이진 탐색 시작
    while left < right:
        mid = (left + right) // 2  # 중간 값을 계산
        # 모든 검사관이 중간 값 시간 내에 검사할 수 있는 사람 수의 합
        total = sum(mid // time for time in times)  
        
        if total >= n:
            # 검사할 수 있는 사람 수가 충분하면 시간을 줄임
            right = mid
        else:
            # 검사할 수 있는 사람 수가 부족하면 시간을 늘림
            left = mid + 1
    
    # 최소 시간이 left에 저장됨
    return left