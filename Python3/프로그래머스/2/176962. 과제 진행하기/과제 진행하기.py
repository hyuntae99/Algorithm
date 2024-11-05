from collections import deque

def solution(plans):
    def trans(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m  # 시간을 분 단위로 변환

    # plans를 시작 시간 기준으로 정렬
    plans.sort(key=lambda x: trans(x[1]))
    
    ans = []
    sub = deque()
    
    for i in range(len(plans)):
        name, start, duration = plans[i][0], plans[i][1], int(plans[i][2])
        current_time = trans(start)
        
        # 다음 과제가 있는 경우 다음 과제의 시작 시간과 비교
        if i < len(plans) - 1:
            next_start = trans(plans[i + 1][1])
            time_available = next_start - current_time  # 현재 과제에서 다음 과제로 이동까지 남은 시간
            
            # 시간이 충분하지 않을 경우 남은 시간을 sub에 저장
            if time_available < duration:
                sub.append((name, duration - time_available))
            else:
                # 시간이 충분할 경우 과제를 완료
                ans.append(name)
                
                # 남은 시간 동안 sub의 과제도 처리
                remaining_time = time_available - duration
                while sub and remaining_time > 0:
                    leftover_name, leftover_time = sub.pop()
                    # 남은 시간이 더 많은 경우
                    if remaining_time >= leftover_time:
                        ans.append(leftover_name)
                        remaining_time -= leftover_time
                    else: # 남은 시간이 없는 경우
                        sub.append((leftover_name, leftover_time - remaining_time))
                        break
        else:
            # 마지막 과제는 바로 완료
            ans.append(name)

    # 남은 과제 처리
    while sub:
        leftover_name, _ = sub.pop()
        ans.append(leftover_name)
    
    return ans
