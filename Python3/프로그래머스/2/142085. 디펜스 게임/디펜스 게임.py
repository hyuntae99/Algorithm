import heapq

def solution(n, k, enemy):
    max_heap = []
    
    for i in range(len(enemy)):
        # 현재 라운드의 적 병력을 최대 힙에 음수로 추가
        heapq.heappush(max_heap, -enemy[i])
        
        # 남은 병력을 감소시킴
        n -= enemy[i] 
        
        # 병력이 없다면
        if n < 0: 
            # 방어권이 있는 경우
            if k > 0: 
                k -= 1
                # 최대 힙에서 가장 큰 병력 제거 (방어권 사용)
                n += -heapq.heappop(max_heap) 
            else:
                return i  # 방어 불가한 라운드 반환
    
    return len(enemy)  # 모든 라운드 방어 가능할 경우
