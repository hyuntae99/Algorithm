import heapq

def solution(jobs):
    answer = 0
    length = len(jobs)
    
    # jobs를 최소 힙으로 변환
    heapq.heapify(jobs)
    time = 0
    heap = []

    # jobs가 비어있지 않은 동안 반복
    while jobs:           
        # 현재 시간까지 도착한 작업들을 힙에 추가
        while jobs:
            x, y = heapq.heappop(jobs)
            if x > time:
                # 아직 도착하지 않은 작업은 다시 jobs에 추가
                heapq.heappush(jobs, [x, y])
                break
            else:
                # 도착한 작업은 작업 소요 시간을 기준으로 힙에 추가
                heapq.heappush(heap, [y, x])

        if len(heap) == 0:
            # 처리할 작업이 없으면 현재 시간 증가
            time += 1
        else:
            # 처리할 작업이 있으면 가장 짧은 작업을 꺼내서 처리
            a, b = heapq.heappop(heap)
            answer += (a + time - b)
            time += a

    # 남아있는 힙의 작업들을 처리
    while heap:
        a, b = heapq.heappop(heap)
        answer += a + time - b
        time += a
        print(time)

    # 평균 대기 시간 반환
    return answer // length