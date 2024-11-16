def solve(arr, ln):
    mx = 0  # 현재 길이에서 가장 긴 회문 길이

    for i in range(MAX-ln+1):
        for j in range(MAX-ln+1):
            # 가로 확인
            row = arr[i][j:j+ln]
            if palindrome(row):
                mx = ln

            # 세로 확인 (범위 초과 방지)
            if i + ln <= MAX:  # 세로 범위를 초과하지 않을 때만 처리
                col = [arr[k][j] for k in range(i, i+ln)]
                if palindrome(col):
                    mx = ln

    return mx

def palindrome(lst):
    s, e = 0, len(lst) - 1

    while s < e:
        if lst[s] != lst[e]:
            return False
        s += 1
        e -= 1

    return True

MAX = 100
T = 10
for _ in range(T):
    test_case = int(input())
    arr = [list(input().strip()) for _ in range(MAX)]  # 글자판 입력

    ans = 1  # 최소 회문 길이
    # 회문의 길이를 2부터 MAX까지 탐색
    for ln in range(2, MAX+1):
        ans = max(ans, solve(arr, ln))  # 가장 긴 회문 길이 갱신

    print(f'#{test_case} {ans}')
