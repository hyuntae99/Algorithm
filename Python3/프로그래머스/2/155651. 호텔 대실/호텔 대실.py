from datetime import datetime, timedelta
import heapq

def solution(book_time):
    answer = 0
    used = set()  # 현재 사용 중인 회의실을 기록하는 집합
    queue = []  # 예약된 회의의 시작 및 종료 시간을 저장하는 힙 (우선순위 큐)
    heapq.heapify(queue)  # 힙 초기화

    # 각 예약의 시작 시간과 종료 시간을 힙에 넣음
    for idx, ele in enumerate(book_time):
        # 회의 시작 시간을 힙에 삽입 (형식: [시작 시간, 인덱스])
        heapq.heappush(queue, [datetime.strptime(ele[0], '%H:%M'), idx])
        # 회의 종료 시간에 9분 59초를 더해서 삽입 (형식: [종료 시간 + 9분 59초, 인덱스])
        heapq.heappush(queue, [datetime.strptime(ele[1], '%H:%M') + timedelta(minutes=9, seconds=59), idx])

    # 힙이 빌 때까지 반복
    while queue:
        bt, idx = heapq.heappop(queue)  # 가장 먼저 처리해야 할 회의 시간 (시작 또는 종료) 가져오기
        if idx not in used:  # 사용 중인 회의실에 해당 회의가 없으면 (새로운 회의 시작)
            used.add(idx)  # 회의실에 해당 회의 추가
            answer = max(answer, len(used))  # 최대 회의실 사용 개수 갱신
        else:  # 이미 사용 중인 회의면 (해당 회의가 종료됨)
            used.remove(idx)  # 회의실에서 회의 제거

    return answer  # 필요한 최소 회의실 개수 반환
