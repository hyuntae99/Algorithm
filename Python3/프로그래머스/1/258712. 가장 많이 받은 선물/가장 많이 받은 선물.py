def solution(friends, gifts):    
    n = len(friends)
    # 사람에게 고유 번호 할당
    people = {friend : i for i, friend in enumerate(friends)} 
    
    # 이차원 배열 생성
    presents = [[0 for _ in range(n)] for _ in range(n)]
    
    for gift in gifts:
        sender, receiver = gift.split(' ')
        # 이차원 배열에 누가 누구에게 줬는지 카운트
        presents[people[sender]][people[receiver]] += 1
        
    scores = [] # 선물 지수
    for i in range(n):
        send = sum(presents[i]) # 준 선물
        receive = 0 # 받은 선물
        for j in range(n):
            receive += presents[j][i]
        scores.append(send - receive) # 선물 지수 계산
        
    max = 0 # 최댓값
    for i in range(n):
        count = 0 # 받을 선물 수
        for j in range(n):
            if i == j:
                continue
            # 내가 준 선물이 더 크다.
            if presents[i][j] > presents[j][i]:
                count += 1
            # 선물 수가 같거나 기록이 없다.
            elif presents[i][j] == presents[j][i]:
                # 선물 지수가 크다.
                if scores[i] > scores[j]:
                    count += 1
        # 최댓값 최신화
        if max < count:
            max = count

    return max