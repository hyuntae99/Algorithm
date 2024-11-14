icp = {'(': 3, '*': 2, '+': 1}
isp = {'*': 2, '+': 1, '(': 0}

# T = int(input())
T = 10
for test_case in range(1, T + 1):
    _ = input()
    st = input()

    equ = ''
    stk = []

    # [1] 중위 -> 후위
    for ch in st:
        if ch.isdigit():
            equ += ch
        else:
            if ch == ')':
                while stk:
                    t = stk.pop()
                    if t == '(':
                        break
                    else:
                        equ += t
            else:  # 연산자
                while stk and icp[ch] <= isp[stk[-1]]:
                    equ += stk.pop()
                stk.append(ch)
    while stk:
        equ += stk.pop()

    # [2] 후위표기식 계산
    for ch in equ:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            op2 = stk.pop()  # op1, 2 순서에 주의!!
            op1 = stk.pop()
            if ch == '*':
                stk.append(op1 * op2)
            elif ch == '+':
                stk.append(op1 + op2)

    print(f'#{test_case} {stk.pop()}')