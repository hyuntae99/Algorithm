def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # 2부터 √n까지 나누어 떨어지는지 확인
        if n % i == 0:
            return False
    return True

def convert_to_base(n, base):
    T = "0123456789ABCDEF"
    if n == 0:
        return "0"
    
    result = ''
    while n > 0:
        result = T[n % base] + result  # 나머지를 앞에 추가
        n //= base  # 몫을 다음 숫자로 설정
    
    return result

def solution(n, k):
    answer = 0
    
    num = convert_to_base(n, k)
    nums = num.split('0')
    
    for word in nums:
        if word != '' and is_prime(int(word)):
            answer += 1
    return answer