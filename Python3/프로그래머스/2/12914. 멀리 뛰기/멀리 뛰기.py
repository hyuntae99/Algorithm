from collections import Counter
from math import factorial

# 같은 것이 있는 순열 함수
def count_unique_permutations(seq):
    # 입력된 리스트의 각 요소의 빈도를 계산
    counter = Counter(seq)
    # 전체 순열의 개수 (요소 개수의 팩토리얼)
    total_permutations = factorial(len(seq))
    # 각 요소의 빈도에 대한 팩토리얼을 나누어 줌
    for count in counter.values():
        total_permutations //= factorial(count)
    
    return total_permutations


def solution(n):
    answer = 0
    two = n // 2 # 2의 개수
    one = n % 2 # 1의 개수
    
    while (two >= 0):
        arr = "2" * two
        arr += "1" * one
        answer += count_unique_permutations(arr) 
        two -= 1
        one += 2
    answer %= 1234567
    return answer