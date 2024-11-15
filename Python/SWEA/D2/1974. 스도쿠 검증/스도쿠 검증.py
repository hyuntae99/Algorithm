def check1(arr):
    # 세로 확인
    for i in range(9):
        if set(arr[j][i] for j in range(9)) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False

    # 가로 확인
    for row in arr:
        if set(row) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False

    return True

def check2(arr):
    points = [(0,0), (3,0), (6,0),
              (0,3), (3,3), (6,3),
              (0,6), (3,6), (6,6)]

    for si, sj in points:
        s = set()
        for i in range(si, si+3):
            for j in range(sj, sj+3):
                s.add(arr[i][j])

        if s != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False

    return True

T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = 0
    if check1(arr) and check2(arr):
        ans = 1
        
    print(f'#{test_case} {ans}')
