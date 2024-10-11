def dfs(n, cnt):
    global ans
    if n == N: # 모든 계란 충돌 완료
        ans = max(ans, cnt)
        return

    if arr[n][0] <= 0: # 손에 든 계란 박살
        dfs(n + 1, cnt)
    else:
        flag = False
        for i in range(N):
            if n == i or arr[i][0] <= 0: # 자기자신이나 내구도가 없는 애들은 패스
                continue

            # 계란 충돌
            flag = True
            arr[n][0] -= arr[i][1]
            arr[i][0] -= arr[n][1]

            dfs(n + 1, cnt + int(arr[n][0] <= 0) + int(arr[i][0] <= 0)) # 내 계란 or 상대 계란이 깨질 경우 각각 추가

            # 복구
            arr[n][0] += arr[i][1]
            arr[i][0] += arr[n][1]

        if flag == False: # 한번도 충돌 x
            dfs(n + 1, cnt) # 다음으로 패스
        

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)] # 내구도, 무게(공격력)

ans = 0
dfs(0, 0) # 계란 인덱스, 파괴 횟수
print(ans)
