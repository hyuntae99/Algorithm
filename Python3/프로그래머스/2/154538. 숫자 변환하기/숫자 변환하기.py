from collections import defaultdict
def solution(x, y, n):
    # 예외처리
    if x == y:
        return 0
    
    d = defaultdict(set) # 중복값 제거
    d[0].add(x) # 초기 설정
    
    for i in range(1, (y//n)+1):
        for num in list(d[i-1]): # 전 단계에 대해서 계산
            if y in (num+n, num*2, num*3):
                return i
            d[i].add(num+n)
            d[i].add(num*2)
            d[i].add(num*3)

    return -1