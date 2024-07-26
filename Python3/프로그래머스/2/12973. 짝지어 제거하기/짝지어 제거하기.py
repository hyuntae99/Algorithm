def solution(s):
    answer = 0
    
    stack = []
    for i in s:
        # 스택이 비어있지 않고, 스택의 top에 있는 문자와 현재 문자가 같다면
        if stack and stack[-1] == i:
            stack.pop() # 제거
            continue
        # 문자와 다르다면 추가
        stack.append(i)
    
    if not stack:
        answer = 1
    return answer
