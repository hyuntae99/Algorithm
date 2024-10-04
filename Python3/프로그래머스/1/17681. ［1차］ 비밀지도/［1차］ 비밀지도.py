def solution(n, arr1, arr2):
    # 2차원 배열 초기화
    answer = [[' ' for _ in range(n)] for _ in range(n)]
    func(arr1, answer, n)
    func(arr2, answer, n)

    secret_map = []
    for ans in answer:
        result = ''
        # 이진법 변환시 필요한 뒤집기 적용
        for i in reversed(ans):
            result += i
        secret_map.append(result)
    return secret_map

def func(arr, answer, n):
    cnt = 0
    for num in arr:
        # n번 반복하면서 2진법으로 변경
        for i in range(n):
            # 1이면 '#'으로 바꾼다.
            if num % 2:
                answer[cnt][i] = '#'
            num //= 2
        cnt += 1