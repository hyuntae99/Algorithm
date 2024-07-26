def solution(n):
    ans = 0
    while n:
        # 짝수의 경우 순간이동 가능
        if n % 2 == 0:
            n /= 2
        # 홀수의 경우 한칸 빼야함
        else:
            n -= 1
            ans += 1
    return ans