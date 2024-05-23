def solution(operations):
    arr = [] # 우선순위 큐
    for operation in operations:
        # 명령어와 숫자 분리
        a, b = operation.split(' ')
        # 숫자 삽입
        if a == 'I':
            arr.append(int(b))
        elif a == 'D':
            if len(arr) != 0:
                # 최솟값 삭제
                if b == '-1':
                    arr.remove(min(arr))
                # 최댓값 삭제
                elif b == '1':
                    arr.remove(max(arr))
    # 우선순위 큐에 비어있다면
    if len(arr) == 0:
        answer = [0, 0]
    else:
        answer = [max(arr), min(arr)]
    
    return answer