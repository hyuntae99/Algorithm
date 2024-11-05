def solution(targets):
    # 끝 지점을 기준으로 오름차순 정렬
    targets.sort(key=lambda x: x[1])

    camera_count = 0
    last_camera_position = -1  # 초기 카메라 위치 (덮는 범위 밖)

    for start, end in targets:
        # 현재 구간이 마지막 카메라 위치로 덮을 수 없는 경우, 새로운 카메라 설치
        if start >= last_camera_position:
            camera_count += 1
            last_camera_position = end  # 새로운 카메라 위치를 현재 구간의 끝에 설치
            # print(last_camera_position)

    return camera_count
