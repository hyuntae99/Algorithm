def solve(arr):
    s = []

    for a in arr:
        # 개행을 만나면 스택에 추가
        if a == '(':
            s.append(')')
        elif a == '[':
            s.append(']')
        elif a == '<':
            s.append('>')
        elif a == '{':
            s.append('}')
        else:
            # 아무것도 없는 상태에서 닫힘 문자 -> 오류
            if len(s) == 0:
                return 0

            # 닫힘 문자와 상단이 맞으면 제거
            if a == s[-1]:
                s.pop()
            else:
                return 0
            
        #print(s)

    if len(s) == 0:
        return 1

    return 0

T = 10
for test_case in range(1,T+1):
    N = int(input())
    arr = str(input()).strip()
    ans = solve(arr)
    print(f'#{test_case} {ans}')