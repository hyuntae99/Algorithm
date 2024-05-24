def solution(people, limit):
    people.sort()
    answer = 0  
    # 투 포인트 설정
    light, heavy = 0, len(people) - 1  

    # light 포인터가 heavy 포인터보다 작거나 같을 때까지 반복
    while light <= heavy:
        # 가장 가벼운 사람과 가장 무거운 사람의 몸무게 합이 제한 무게 이하인 경우 둘 다 탑승
        if people[light] + people[heavy] <= limit:
            light += 1  # 가벼운 사람 탑승
        heavy -= 1 # 무거운 사람 탑승
        answer += 1  # 구명보트 수 증가

    return answer  # 필요한 총 구명보트 수를 반환
