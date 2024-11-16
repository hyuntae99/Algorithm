def solve(arr):
    for i in range(4):
        for j in range(4):
            dfs(i,j,arr[i][j]) # 완전 탐색

def dfs(si,sj,lst):
    # 일정 길이가 되면 저장
    if len(lst) == 7:
        ans.add(lst)
        return

    # 4방향 탐색
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = si+di, sj+dj
        # 범위내 (추가 제약x)
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni,nj,lst+arr[ni][nj])

T = int(input())
for test_case in range(1,T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    ans = set()
    solve(arr)
    # print(ans)
    print(f'#{test_case} {len(ans)}')