def solution(n, stations, w):
    # 설치해야 할 기지국 개수
    ans = 0
    
    # 현재 위치를 1부터 시작
    current = 1
    
    # 각 기지국이 커버하는 범위 계산
    for s in stations:
        # 현재 위치부터 기지국의 왼쪽 범위까지의 거리 계산
        if current < s - w:
            # 커버되지 않는 구간의 길이
            length = (s - w) - current
            # 필요한 기지국 개수 계산
            ans += (length + (2 * w)) // (2 * w + 1)
        
        # 기지국 범위 다음으로 current 이동
        current = s + w + 1
    
    # 마지막 기지국 이후 남은 구간 처리
    if current <= n:
        length = n - current + 1
        ans += (length + (2 * w)) // (2 * w + 1)
    
    return ans
