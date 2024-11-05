import math

def solution(k, d):
    count = 0
    for x in range(0, d + 1, k):
        # x에 대해 가능한 최대 y 값 계산
        max_y = math.isqrt(d**2 - x**2)
        # y 값의 개수를 더해줌 (y 값이 k 간격으로 존재)
        count += (max_y // k) + 1
    return count
