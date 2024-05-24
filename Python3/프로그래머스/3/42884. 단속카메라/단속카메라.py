def solution(routes):
    routes.sort(key=lambda x: x[1]) # 끝 지점 기준으로 정렬
    answer = 0
    camera_position = -30001  # 현재 카메라 위치를 설정 
    
    for route in routes:
        # 카메라가 가장 작은 위치보다 작으면
        if camera_position < route[0]:
            answer += 1 # 추가
            camera_position = route[1]  # 가장 먼 위치에 카메라를 설치
    
    return answer