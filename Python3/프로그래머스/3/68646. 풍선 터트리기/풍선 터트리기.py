def solution(a):
    n = len(a)
    if n <= 2:
        return n  # 풍선이 2개 이하인 경우 모두 남길 수 있음

    # 왼쪽과 오른쪽 최소값 배열 생성
    left_min = [0] * n
    right_min = [0] * n

    left_min[0] = a[0]
    right_min[-1] = a[-1]

    # 왼쪽 최소값 배열 계산
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], a[i])

    # 오른쪽 최소값 배열 계산
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])

    # 남길 수 있는 풍선 개수 세기
    answer = 0
    for i in range(n):
        # 왼쪽 또는 오른쪽 중 하나의 최소값보다 작거나 같으면 남길 수 있음
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1

    return answer
