def solution(number, k):
    stack = []
    
    for num in number:
        # 스택의 최상단이 num보다 작을 경우
        while stack and k > 0 and stack[-1] < num:
            stack.pop() # 제거
            k -= 1 # 삭제 횟수 차감
        stack.append(num) # 스택에 추가
    
    # k가 아직 남아있는 경우 내림차순으로 뒤에를 제거
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)