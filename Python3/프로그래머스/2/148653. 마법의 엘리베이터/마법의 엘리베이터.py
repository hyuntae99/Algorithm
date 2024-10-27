def solution(storey):
    ans = 0
    while storey > 0:
        remainder = storey % 10
        # 나머지가 5보다 크거나 나머지가 5이고 앞자리 수도 5이상인 경우
        if remainder > 5 or (remainder == 5 and (storey // 10) % 10 >= 5):
            ans += (10 - remainder)
            storey = (storey // 10) + 1  # 자릿수를 하나 올림
        else:
            ans += remainder
            storey //= 10  # 다음 자릿수로 이동
            
    return ans
