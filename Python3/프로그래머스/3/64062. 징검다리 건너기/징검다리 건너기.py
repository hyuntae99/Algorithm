from collections import deque

def solution(stones, k):
    q = deque()
    answer = float('inf')

    for i, stone in enumerate(stones):
        # 1. Deque의 뒤에서부터 현재 값보다 작은 값들을 제거
        while q and q[-1][1] < stone:
            q.pop()

        # 2. 현재 값을 Deque에 추가
        q.append((i, stone))

        # 3. Deque의 첫 번째 원소가 윈도우 범위를 벗어나면 제거
        if q[0][0] <= i - k:
            q.popleft()

        # 4. 윈도우 크기가 k에 도달하면 answer 업데이트
        if i >= k - 1:
            answer = min(answer, q[0][1])  # 현재 윈도우에서 최대값 중 가장 작은 값 찾기

    return answer
