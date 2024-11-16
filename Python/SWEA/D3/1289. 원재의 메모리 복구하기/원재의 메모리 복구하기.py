def solve(arr):
    cnt = 0
    cbit = '0'

    for bit in arr:
        if bit != cbit:  # 비트가 변경될 때만
            cnt += 1
            cbit = bit  # 현재 비트 상태 업데이트
            
    return cnt

T = int(input())
for test_case in range(1, T+1):
    arr = input().strip()
    ans = solve(arr)
    print(f"#{test_case} {ans}")
