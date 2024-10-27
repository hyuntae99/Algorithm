from collections import Counter
from itertools import combinations

def solution(orders, course):
    result = []
    
    for c in course:
        comb_counter = Counter()  # 조합을 저장할 Counter
        for order in orders:
            order = sorted(order)
            # c개의 메뉴 조합을 찾아 Counter에 추가
            # (A,C) : 4 / (C,D) : 3 ...
            comb_counter.update(combinations(order, c))  
        
        # 가장 많이 나온 조합이 2번 이상일 때만 결과에 추가
        if comb_counter:
            max_count = max(comb_counter.values())
            if max_count > 1:
                for comb in comb_counter:
                    if comb_counter[comb] == max_count:
                        result.append(''.join(comb))
                        
    return sorted(result)  # 최종 결과는 사전 순 정렬
