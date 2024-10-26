def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            # 짝수일 경우: number + 1
            answer.append(number + 1)
        else:
            # 홀수일 경우: 마지막 0을 1로 바꾸고 그 다음 1을 0으로
            bit = '0' + bin(number)[2:]  # 앞에 '0'을 붙여 처리
            idx = bit.rfind('0')  # 가장 마지막 0의 위치 찾기
            bit = list(bit)
            bit[idx] = '1'
            bit[idx + 1] = '0'
            answer.append(int(''.join(bit), 2))

    return answer
