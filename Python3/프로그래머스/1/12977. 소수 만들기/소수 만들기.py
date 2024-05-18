import itertools

def solution(nums):
    answer = 0
    cases = itertools.combinations(nums, 3)
    
    for case in cases:
        num = sum(case)
        if myDivisor(num) == 2:
            answer += 1

    return answer

def myDivisor(num):
    cnt = 0
    for i in range(1, int(num**(1/2)) + 1):
        if cnt > 2:
            break
        if num % i == 0:
            cnt += 1
            if i < num // i:
                cnt += 1
    return cnt