from collections import deque

def solution(queue1, queue2):
    # 큐를 덱(deque)으로 변환하여 양방향 삽입/삭제를 쉽게 함
    q1, q2 = deque(queue1), deque(queue2)
    
    # 두 큐의 원소 합을 계산하여 총합이 홀수면 불가능하므로 -1 반환
    total = sum(q1) + sum(q2)
    if total % 2 != 0:
        return -1
    
    # 목표 합은 두 큐 합의 절반
    target = total // 2
    sum_q1 = sum(q1)  # q1의 현재 합
    moves = 0  # 이동 횟수
    n = len(q1)  # 각 큐의 길이
    l_q1, l_q2 = 0, 0  # 두 큐에서 이동할 때 인덱스처럼 사용

    # 최대 두 큐의 길이만큼 반복, 그 이상 되면 불가능으로 간주
    while l_q1 < 2 * n and l_q2 < 2 * n:
        if sum_q1 == target:
            return moves 
        elif sum_q1 > target:
            # q1의 합이 목표보다 크면, q1에서 q2로 원소 이동
            sum_q1 -= q1[0]
            q2.append(q1.popleft())
            l_q1 += 1 
        else:
            # q1의 합이 목표보다 작으면, q2에서 q1로 원소 이동
            sum_q1 += q2[0]
            q1.append(q2.popleft())
            l_q2 += 1 
        moves += 1  # 이동 횟수 증가
    
    return -1  
