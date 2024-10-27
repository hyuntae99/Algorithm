from collections import defaultdict

def solution(weights):
    answer = 0
    
    # defaultdict를 사용하여 무게별 카운트를 저장
    d = defaultdict(int)
    
    # 무게들을 오름차순으로 정렬
    weights.sort()
    
    for weight in weights:
        # 현재 무게와 조건에 맞는 비율을 만족하는 쌍이 있는지 확인
        if d[weight]:
            answer += d[weight]
        
        # 1:1 비율의 쌍을 고려
        d[weight] += 1
        
        # 3:2 비율을 만족하는 경우
        if weight % 2 == 0:
            d[(weight//2)*3] += 1
            
        # 4:3 비율을 만족하는 경우
        if weight % 3 == 0: 
            d[(weight//3)*4] += 1
        
        # 2:1 비율을 만족하는 경우
        d[weight*2] += 1

    return answer
