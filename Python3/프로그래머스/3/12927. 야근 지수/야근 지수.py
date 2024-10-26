def solution(n, works):
    while True:
        # 일할 시간이 없거든 더 이상 일을 할 필요가 없을 때 종료
        if n == 0 or works[0] == 0:
            break
            
        works.sort(reverse=True)
        mx = works[0]
        for i in range(len(works)):
            # 최댓값을 지나면 중단
            if works[i] != mx:
                break
            
            # 아직 일을 할 수 있다면
            if n > 0:
                works[i] -= 1 # 작업량 감소
                n -= 1 # 피로도 감소
            else:
                break
                
    ans = [x**2 for x in works] # 피로도 계산을 위한 배열
    return sum(ans)