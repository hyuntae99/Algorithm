import math

def solution(n, k):
    # 사용할 숫자들 (1부터 n까지)
    arr = [i for i in range(1, n + 1)]
    result = []

    # k를 인덱스 기준으로 변경 (0-based index)
    k -= 1

    # 남은 숫자와 k값을 이용해 각 자리를 결정
    for i in range(n, 0, -1):
        # 현재 자리에서 선택할 숫자의 인덱스 계산
        fact = math.factorial(i - 1)
        index = k // fact
        result.append(arr.pop(index))
        
        # k 값을 업데이트하여 다음 자리로 이동
        k %= fact

    return result