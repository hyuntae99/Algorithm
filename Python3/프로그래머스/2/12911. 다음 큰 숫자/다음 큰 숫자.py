def solution(n):
    # n을 2진수로 변환 후 1의 개수 저장
    n_count1 = bin(n).count('1')
    # n 다음 숫자
    next_n = n + 1
    
    while True:
        # n 다음 숫자의 1의 숫자가 똑같다면 종료
        if n_count1 == bin(next_n).count('1'):
            return next_n
        # 아니면 다음 숫자로 
        next_n += 1
    return next_n