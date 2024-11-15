def dfs(depth):
    global ans
    if int(cnt) == depth:
        ans = max(ans, int("".join(nums)))
        return

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]  # 교환

            check_number = int(''.join(nums))  # 교환된 숫자 만들기

            if (check_number, depth) not in v:
                v.append((check_number, depth))  # 현재 깊이와 교환 숫자 넣기
                dfs(depth + 1)  # 교환 후 깊이 진행
            nums[i], nums[j] = nums[j], nums[i]  # 다시 백트레킹으로 되돌리기


T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    v = []
    nums, cnt = map(int, input().split())
    nums = list(str(nums))
    # dfs를 이용하여 모든 경우의 수를 생각
    # dfs 의 깊이는 changeCount로 생각
    dfs(0)
    print(f'#{test_case} {ans}')