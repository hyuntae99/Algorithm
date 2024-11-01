from itertools import permutations

def calculate(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def evaluate(expression, operators):
    # 숫자와 연산자를 분리
    numbers, ops = [], []
    num = ''
    for char in expression:
        # 숫자일 경우, 추가
        if char.isdigit():
            num += char
        else:
            # 숫자가 아니면 이전 숫자 추가 + 연산자 추가
            numbers.append(int(num))
            ops.append(char)
            num = ''
    numbers.append(int(num)) # 마지막 숫자 처리

    # 각 우선순위에 따라 계산
    for op in operators:
        stack_nums, stack_ops = [numbers[0]], []
        for i in range(len(ops)):
            stack_ops.append(ops[i])
            stack_nums.append(numbers[i + 1])
            # 우선 연산자를 만나면 계산
            if stack_ops[-1] == op:
                b, a = stack_nums.pop(), stack_nums.pop()
                stack_nums.append(calculate(op, a, b))
                stack_ops.pop()

        numbers, ops = stack_nums, stack_ops
    
    return abs(numbers[0])

def solution(expression):
    # 가능한 연산자 순서의 모든 조합을 생성
    operator_orders = list(permutations(['+', '-', '*']))
    max_result = 0
    
    # 각 우선순위로 계산하여 최대 절댓값을 찾음
    for operators in operator_orders:
        max_result = max(max_result, evaluate(expression, operators))
    
    return max_result
