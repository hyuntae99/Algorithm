def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = truck_weights # 트럭 무게
    bridge = [0] * bridge_length # 다리
    total_weigtht = 0 # 다리 위의 총 트럭 무게
    
    while bridge:
        time += 1 # 시간 증가
        total_weigtht -= bridge.pop(0) # 가장 앞의 무게를 제거
        if trucks:
            # 다음 트럭까지 다리에 올라와도 괜찮다면
            if total_weigtht + trucks[0] <= weight:
                total_weigtht += trucks[0] # 총 무게에 트럭 추가
                bridge.append(trucks.pop(0)) # 다리에 트럭 추가  
            # 여유가 없다면
            else:
                bridge.append(0) # 무게 0 추가

    return time