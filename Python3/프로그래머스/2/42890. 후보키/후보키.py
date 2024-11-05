from itertools import combinations

def solution(relation):
    row_count = len(relation)
    col_count = len(relation[0])

    # 가능한 모든 컬럼 인덱스 조합
    all_combinations = []
    for i in range(1, col_count + 1):
        all_combinations.extend(combinations(range(col_count), i))
    
    # 유일성 및 최소성을 만족하는 후보키 저장
    candidate_keys = []
    
    for comb in all_combinations:
        # 유일성 검사: 각 튜플의 값 조합을 set에 저장하여 중복 여부 확인
        seen = set()
        for row in relation:
            key = tuple(row[i] for i in comb)  # comb에 해당하는 속성 값만 추출하여 튜플로 저장
            seen.add(key)
        
        # 유일성 만족 여부 확인
        if len(seen) == row_count:
            # 최소성 검사
            is_minimal = True
            for candidate in candidate_keys:
                if set(candidate).issubset(comb):  # 기존 후보키가 새로운 후보키의 부분 집합인지 확인
                    is_minimal = False
                    break
            
            if is_minimal:
                candidate_keys.append(comb)

    return len(candidate_keys)
