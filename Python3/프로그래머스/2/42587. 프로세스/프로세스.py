def solution(priorities, location):
    answer = []
    priorities_sorted = sorted(priorities, reverse=True)
    
    idx = 0
    while priorities_sorted:
        # 프로세스의 우선순위가 가장 높을 경우
        if priorities[idx % len(priorities)] == priorities_sorted[0]:
            answer.append(idx % len(priorities)) # 실행하고
            priorities_sorted.pop(0) # 다음으로 높은 우선순위로 만들기 위해 제거
        idx += 1
    
    return answer.index(location) + 1