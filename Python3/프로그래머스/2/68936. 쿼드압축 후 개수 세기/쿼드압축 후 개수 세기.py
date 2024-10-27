def solution(arr):
    # 전역 변수로 사용할 정답 배열 선언 (0과 1의 개수를 저장할 배열)
    global answer
    answer = [0, 0]  # answer[0]은 0의 개수, answer[1]은 1의 개수
    quad(arr, [0, 0], len(arr))  # 배열 전체를 시작점으로 쿼드트리 분할 시작
    return answer  # 0과 1의 개수를 반환

def quad(arr, s, n):
    # s: 시작 좌표 (x, y), n: 현재 배열의 크기
    x, y = s[0], s[1]  # 시작 좌표 설정
    tg = arr[x][y]  # 현재 영역의 첫 번째 값을 기준으로 설정 (전체 영역이 같은지 비교할 기준값)
    
    # 현재 영역 내 모든 값이 동일한지 확인하는 반복문
    for i in range(n):
        for j in range(n):
            # 하나라도 기준 값과 다른 값이 있다면 더 작은 영역으로 분할
            if arr[x + i][y + j] != tg:
                # 4개의 하위 영역으로 분할하여 재귀 호출
                quad(arr, [x, y], n // 2)  # 좌상단 영역
                quad(arr, [x, y + n // 2], n // 2)  # 우상단 영역
                quad(arr, [x + n // 2, y], n // 2)  # 좌하단 영역
                quad(arr, [x + n // 2, y + n // 2], n // 2)  # 우하단 영역
                return  # 하위 영역으로 분할했으므로 더 이상의 처리는 필요하지 않음

    # 모든 값이 동일하면 해당 값의 개수를 증가시킴
    answer[tg] += 1  # tg가 0이면 answer[0]이, 1이면 answer[1]이 증가
