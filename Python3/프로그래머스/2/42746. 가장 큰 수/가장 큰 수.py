from functools import cmp_to_key

# x <= y일 때 1, x > y일 때 -1
def compare(x, y):
    if str(y) + str(x) >= str(x) + str(y):
        return 1
    else:
        return -1

def solution(numbers):
    # 사용자 지정 함수로 정렬
    numbers = sorted(numbers, key = cmp_to_key(compare))
    return str(int("".join(map(str, numbers))))