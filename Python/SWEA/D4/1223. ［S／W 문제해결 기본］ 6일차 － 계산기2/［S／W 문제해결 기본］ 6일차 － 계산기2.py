pri = {'*': 2, '+': 1}
# T = int(input())
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    st = input()

    equ = ''
    stk = []
    # [1] 중위 -> 후위표기식
    for ch in st:
        if ch.isdigit():  # 숫자일 경우
            equ += ch
        else:
            while stk and pri[ch] <= pri[stk[-1]]:
                equ += stk.pop()
            stk.append(ch)
    while stk:
        equ += stk.pop()

    # [2] 후위연산식 계산
    for ch in equ:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            op2 = stk.pop()
            op1 = stk.pop()
            if ch == '*':
                stk.append(op1 * op2)
            elif ch == '+':
                stk.append(op1 + op2)

    print(f'#{test_case} {stk.pop()}')