from itertools import permutations

def is_match(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    
    for i in range(len(user_id)):
        if banned_id[i] != '*' and user_id[i] != banned_id[i]:
            return False
    return True

def solution(user_id, banned_id):
    result = set()  # 중복을 막기 위한 set
    
    # 순열로 모든 경우의 수 계산 -> 최대 = 8P8 = 8! = 40320
    for perm in permutations(user_id, len(banned_id)):
        match = True
        for i in range(len(banned_id)):
            # 한번이라도 매칭이 안된다면 실패
            if not is_match(perm[i], banned_id[i]):
                match = False
                break
        
        if match:
            # 순서를 무시하기 위해 정렬한 튜플을 set에 추가
            # (frodo, crodo, abc123) = (crodo, frodo, abc123)
            result.add(tuple(sorted(perm)))  

    return len(result)
