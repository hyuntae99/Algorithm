def solve():
    cnt = 0
    for i in range(8):
        for j in range(8):
            if j <= 8-N and check_row(i,j,N):
                cnt += 1
            if i <= 8-N and check_col(i,j,N):
                cnt += 1
    return cnt

# 가로 체크
def check_row(i,j,N):
    lst = arr[i][j:j+N]
    if palindrome(lst):
        return True
    return False

# 세로 체크
def check_col(i,j,N):
    lst = [arr[i+idx][j] for idx in range(N)]
    if palindrome(lst):
        return True
    return False

# 회문 체크
def palindrome(lst):
    s,e = 0,N-1

    while s < e:
        if lst[s] != lst[e]:
            return False
        s += 1
        e -= 1

    return True

T = 10
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]

    ans = solve()
    print(f'#{test_case} {ans}')
