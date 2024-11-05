def solution(w, h):
    # 최대 공약수
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    n = gcd(w, h)
    us = w + h - n # 사용할 수 없는 정사각형 수 계산
    ts = w * h # 전체 정사각형 수
    
    return ts - us
