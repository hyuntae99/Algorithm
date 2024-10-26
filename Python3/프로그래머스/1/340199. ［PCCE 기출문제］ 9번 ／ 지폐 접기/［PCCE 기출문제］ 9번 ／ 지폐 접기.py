def solution(wallet, bill):
    cnt = 0
    wx,wy = wallet[0],wallet[1]
    bx,by = bill[0],bill[1]
    while True:
        if (wx >= bx and wy >= by) or (wx >= by and wy >= bx):
            return cnt
        else:
            if bx > by:
                bx //= 2
            else:
                by //= 2    
        cnt += 1

        
    return -1 # 여기 올 일은 없겠지만...