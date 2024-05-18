def solution(number, limit, power):
    answer = 0
    for num in range(1, number + 1):
        attack = myDivisor(num, limit)
        if attack > limit:
            answer += power 
        else:
            answer += attack

    return answer

def myDivisor(number, limit):
    cnt = 0
    for i in range(1, int(number**(1/2)) + 1):
        if cnt > limit:
            break
        if number % i == 0:
            cnt += 1
            if i < number//i:
                cnt += 1
    return cnt