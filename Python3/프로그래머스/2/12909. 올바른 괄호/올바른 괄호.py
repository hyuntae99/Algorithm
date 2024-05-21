def solution(s):
    answer = True
    
    cnt = 0
    for i in s:
        if cnt == -1:
            return False
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
            
    if cnt != 0:
        return False

    return True