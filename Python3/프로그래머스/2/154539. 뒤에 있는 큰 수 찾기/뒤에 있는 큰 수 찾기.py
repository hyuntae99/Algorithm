def solution(numbers):
    ans = [-1] * len(numbers)  # 기본값은 -1로 설정
    stack = []

    for i, num in enumerate(numbers):
        # 스택이 비어있지 않고 현재 숫자가 스택의 top이 가리키는 숫자보다 크다면
        while stack and numbers[stack[-1]] < num:
            idx = stack.pop()  # 스택에서 인덱스를 꺼내고
            ans[idx] = num     # 해당 인덱스의 값을 현재 숫자로 갱신
        stack.append(i)  # 현재 인덱스를 스택에 추가

    return ans
