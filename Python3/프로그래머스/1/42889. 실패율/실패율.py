def solution(N, stages):
    rates = {}
    user = len(stages)  # 총 사용자 수

    for stage in range(1, N + 1):
        count = stages.count(stage)  # 해당 스테이지에 있는 사용자 수
        if user > 0:
            failure_rate = count / user  # 실패율 계산
            rates[stage] = failure_rate
        else:
            rates[stage] = 0  # 도달한 사용자가 없으면 실패율 0
        user -= count  # 다음 스테이지로 넘어갈 때 남은 사용자 수 감소

    # 실패율을 기준으로 내림차순 정렬 후, 스테이지 번호 반환
    return sorted(rates, key=lambda x: rates[x], reverse=True)
