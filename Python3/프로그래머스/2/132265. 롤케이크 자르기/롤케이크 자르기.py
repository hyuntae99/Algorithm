from collections import defaultdict

def solution(topping):
    ans = 0
    
    s = set()
    s.add(topping[0])
    
    e = defaultdict(int)
    for t in topping[1:]:
        e[t] += 1
    
    scnt = 1
    ecnt = len(e)
    
    for t in topping[1:]:
        if t not in s: # 없던 숫자라면 
            scnt += 1 # 종류 증가
            s.add(t) # 추가
        
        e[t] -= 1 # 두번째 배열에서 하나 제거
        # 해당 숫자가 더이상 존재하지 않는다면
        if e[t] == 0:
            ecnt -= 1
        
        # 양 배열의 종류가 같다면
        if scnt == ecnt:
            ans += 1

    return ans
